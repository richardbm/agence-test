from rest_framework import viewsets, views
from desempenho import models as desempehno_models
from desempenho import serializers as desempehno_serializer
from datetime import datetime
from collections import OrderedDict
from django.db import connection
from rest_framework.response import Response


class ConsultorViewSet(viewsets.ModelViewSet):
    queryset = desempehno_models.CaoUsuario.objects.all()
    serializer_class = desempehno_serializer.ConsultorSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(permissions__co_sistema=1,
                                    permissions__in_ativo="S",
                                    permissions__co_tipo_usuario__in=[0, 1, 2])
        return queryset


class RelatorioView(views.APIView):
    """
    SELECT us.co_usuario, us.no_usuario,
           date_trunc('month', f.data_emissao) as date_month,
           SUM(f.valor-(f.valor*f.total_imp_inc/100)) as receita,
           sa.brut_salario as custo_fixo,
           SUM((f.valor-(f.valor*f.total_imp_inc/100))*f.comissao_cn/100) as comissao,
           SUM(f.valor-(f.valor*f.total_imp_inc/100)-(sa.brut_salario+((f.valor-(f.valor*f.total_imp_inc/100))*f.comissao_cn/100))) as lucro
        FROM desempenho_caofatura f
          INNER JOIN desempenho_caoos os ON f.co_os_id=os.co_os
          INNER JOIN desempenho_caousuario us ON os.co_usuario_id=us.co_usuario
          INNER JOIN desempenho_caosalario sa ON us.co_usuario=sa.co_usuario_id
        WHERE (data_emissao >= '2007-01-01' AND data_emissao < '2008-03-01')
              AND (os.co_usuario_id='renato.pereira' OR os.co_usuario_id='anapaula.chiodaro')
    GROUP BY us.no_usuario, us.co_usuario, date_trunc('month', data_emissao), custo_fixo
    ORDER BY us.no_usuario, date_month;

    """
    def get(self, request, *args, **kwargs):
        max_date, min_date, user_id = self.get_filters(request)

        if not user_id:
            return Response("Debe seleccionar al menos un consultor", status=400)
        if not min_date:
            return Response("la fecha mínima es requerida", status=400)
        if not max_date:
            return Response("la fecha máxima es requerida", status=400)

        cursor = self.perform_query(max_date, min_date, user_id)

        data = self.serialize_data(cursor)
        return Response(data, status=200)

    def serialize_data(self, cursor):
        list_consultores = []
        relatorio = []
        data = cursor.fetchone()
        while data:
            monthly_data = self.create_monthly_data(data)
            relatorio.append(monthly_data)
            temp_data = cursor.fetchone()
            if not temp_data or data[0] != temp_data[0]:
                consultor_data = self.create_data_consultor(data, relatorio)
                list_consultores.append(consultor_data)
                relatorio = []
            data = temp_data
        return list_consultores

    def create_data_consultor(self, data, relatorio):
        consultor_data = OrderedDict({
            'co_usuario': data[0],
            'no_usuario': data[1],
            'relatorio': relatorio
        })
        return consultor_data

    def create_monthly_data(self, data):
        return OrderedDict({
            "date_month": data[2],
            "receita": data[3],
            "custo_fixo": data[4],
            "comissao": data[5],
            "lucro": data[6],
        })

    def perform_query(self, max_date, min_date, user_id):
        sql_query = self.create_query(max_date, min_date, user_id)
        cursor = connection.cursor()
        cursor.execute(sql_query)
        return cursor

    def create_query(self, max_date, min_date, user_id):
        sql_query = """
        SELECT us.co_usuario, us.no_usuario, 
               date_trunc('month', f.data_emissao) as date_month,
               SUM(f.valor-(f.valor*f.total_imp_inc/100)) as receita,
               sa.brut_salario as custo_fixo,
               SUM((f.valor-(f.valor*f.total_imp_inc/100))*f.comissao_cn/100) as comissao,
               SUM(f.valor-(f.valor*f.total_imp_inc/100)-(sa.brut_salario+((f.valor-(f.valor*f.total_imp_inc/100))*f.comissao_cn/100))) as lucro
            FROM desempenho_caofatura f 
              INNER JOIN desempenho_caoos os ON f.co_os_id=os.co_os
              INNER JOIN desempenho_caousuario us ON os.co_usuario_id=us.co_usuario
              INNER JOIN desempenho_caosalario sa ON us.co_usuario=sa.co_usuario_id
            WHERE (data_emissao >= '{min_date}' AND data_emissao < '{max_date}')
                  AND {list_user}
        GROUP BY us.no_usuario, us.co_usuario, date_trunc('month', data_emissao), custo_fixo
        ORDER BY us.no_usuario, date_month;                                             

        """.format(min_date=min_date, max_date=max_date, list_user=user_id)
        return sql_query

    def get_filters(self, request):
        consultor_ids = request.GET.get("consultor_id", None)
        consultor_ids = consultor_ids.split(",")
        if consultor_ids:
            consultor_ids = "' OR os.co_usuario_id='".join(consultor_ids)
        consultor_ids = "(os.co_usuario_id='" + consultor_ids + "')"
        min_date = request.GET.get('min_date', None)
        max_date = request.GET.get('max_date', None)
        if min_date:
            min_date = datetime.strptime(min_date, "%Y-%m-%d")
        if max_date:
            max_date = datetime.strptime(max_date, "%Y-%m-%d")
        return max_date, min_date, consultor_ids



