from rest_framework import viewsets
from desempenho import models as desempehno_models
from desempenho import serializers as desempehno_serializer
from datetime import datetime
from django.db.models.functions import TruncMonth
from django.db.models import Sum, F


class ConsultorViewSet(viewsets.ModelViewSet):
    queryset = desempehno_models.CaoUsuario.objects.all()
    serializer_class = desempehno_serializer.ConsultorSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(permissions__co_sistema=1,
                                    permissions__in_ativo="S",
                                    permissions__co_tipo_usuario__in=[0, 1, 2])
        return queryset


class RelatorioViewSet(viewsets.ModelViewSet):
    queryset = desempehno_models.CaoFatura.objects.all()
    serializer_class = desempehno_serializer.ConsultorSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        min_date = self.request.GET.get('min_date','')
        max_date = self.request.GET.get('max_date','')
        if min_date!='':
            min_date = datetime.strptime(min_date,"%Y-%m-%d")
        if max_date!='':
            max_date = datetime.strptime(max_date,"%Y-%m-%d")

        consultor_ids = self.request.data.get("consultor_id")
        queryset = queryset.filter(co_os__co_usuario__in=consultor_ids,
                                   data_emissao__gte=min_date,
                                   data_emissao__lte=max_date)
        queryset = queryset.annotate(dates=TruncMonth('data_emissao'),
                                     val=F('valor') - (F('valor') * F('total_imp_inc') / 100)) \
                            .annotate(receita=Sum('val'))\
                            .values("co_os__co_usuario", "dates", "sum")
        return queryset


