from django.db import models


class CaoUsuario(models.Model):
    co_usuario = models.CharField(max_length=20, primary_key=True)
    no_usuario = models.CharField(max_length=50, blank=True, default='')
    ds_senha = models.CharField(max_length=14, blank=True, default='')
    co_usuario_autorizacao = models.CharField(max_length=20, blank=True, null=True)
    nu_matricula = models.BigIntegerField(default=0)
    dt_nascimento = models.DateField(blank=True, null=True)
    dt_admissao_empresa = models.DateField(blank=True, null=True)
    dt_desligamento = models.DateField(blank=True, null=True)
    dt_inclusao = models.DateTimeField(blank=True, null=True)
    dt_expiracao = models.DateField(blank=True, null=True)
    nu_cpf = models.CharField(max_length=14, blank=True, null=True)
    nu_rg = models.CharField(max_length=20, blank=True, null=True)
    no_orgao_emissor = models.CharField(max_length=10, blank=True, null=True)
    uf_orgao_emissor = models.CharField(max_length=2, blank=True, null=True)
    ds_endereco = models.CharField(max_length=150, blank=True, null=True)
    no_email = models.CharField(max_length=100, blank=True, null=True)
    no_email_pessoal = models.CharField(max_length=100, blank=True, null=True)
    nu_telefone = models.CharField(max_length=64, blank=True, null=True)
    dt_alteracao = models.DateField(blank=True, null=True)
    url_foto = models.TextField(blank=True, null=True)
    instant_messenger = models.CharField(max_length=80, blank=True, null=True)
    icq = models.PositiveIntegerField(null=True)
    msn = models.CharField(max_length=50, blank=True, null=True)
    yms = models.CharField(max_length=50, blank=True, null=True)
    ds_comp_end = models.CharField(max_length=50, blank=True, null=True)
    ds_bairro = models.CharField(max_length=30, blank=True, null=True)
    nu_cep = models.CharField(max_length=10, blank=True, null=True)
    no_cidade = models.CharField(max_length=50, blank=True, null=True)
    uf_cidade = models.CharField(max_length=2, blank=True, null=True)
    dt_expedicao = models.DateField(blank=True, null=True)

    class Meta:
        unique_together = ("co_usuario", "no_usuario", "dt_alteracao",)

PERM_CHOICE = (
    ('S', 'Inactivo'),
)


class PermissaoSistema(models.Model):
    co_usuario = models.CharField(max_length=20, primary_key=True)
    co_tipo_usuario = models.BigIntegerField(default=0)
    co_sistema = models.BigIntegerField(default=0)
    in_ativo = models.CharField(max_length=1, default="S", choices=PERM_CHOICE),
    co_usuario_atualizacao = models.CharField(max_length=20, blank=True, null=True),
    dt_atualizacao = models.DateTimeField(blank=True, null=True)
  
    class Meta:
        unique_together = ("co_usuario", "co_tipo_usuario",
                           "co_sistema", "dt_atualizacao")


class CaoOs(models.Model):
    co_os = models.IntegerField(primary_key=True)
    nu_os = models.IntegerField(null=True)
    co_sistema = models.IntegerField(default=0)
    co_usuario = models.CharField(default='0', max_length=50)
    co_arquitetura = models.IntegerField(default=0)
    ds_os = models.CharField(max_length=200, default='0')
    ds_caracteristica = models.CharField(max_length=200, default='0')
    ds_requisito = models.CharField(max_length=200, blank=True, null=True)
    dt_inicio = models.DateField(blank=True, null=True)
    dt_fim = models.DateField(blank=True, null=True)
    co_status = models.IntegerField(default=0)
    diretoria_sol = models.CharField(max_length=50, default='0')
    dt_sol = models.DateField(blank=True, null=True)
    nu_tel_sol = models.CharField(default='0', max_length=20)
    ddd_tel_sol = models.CharField(blank=True, null=True, max_length=5)
    nu_tel_sol2 = models.CharField(blank=True, null=True, max_length=20)
    ddd_tel_sol2 = models.CharField(blank=True, null=True, max_length=5)
    usuario_sol = models.CharField(default='0', max_length=50)
    dt_imp = models.DateField(blank=True, null=True)
    dt_garantia = models.DateField(blank=True, null=True)
    co_email = models.IntegerField(null=True)
    co_os_prospect_rel = models.IntegerField(null=True)


class CaoSalario(models.Model):
    co_usuario = models.CharField(primary_key=True, max_length=20,
                                  blank=True, default='')
    dt_alteracao = models.DateField(blank=True, null=True)
    brut_salario = models.FloatField(default=0)
    liq_salario = models.FloatField(default=0)
