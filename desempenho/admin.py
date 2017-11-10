from django.contrib import admin
from desempenho import models
# Register your models here.

admin.site.register(models.CaoFatura)
admin.site.register(models.PermissaoSistema)
admin.site.register(models.CaoSalario)
admin.site.register(models.CaoUsuario)
admin.site.register(models.CaoOs)