from rest_framework import serializers
from desempenho import models as desempenho_models


class ConsultorSerializer(serializers.ModelSerializer):

    class Meta:
        model = desempenho_models.CaoUsuario
        fields = "__all__"