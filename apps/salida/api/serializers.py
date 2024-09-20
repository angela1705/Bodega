from apps.salida.models import Salida
from rest_framework.serializers import ModelSerializer

class SalidaSerializer(ModelSerializer):
    class Meta:
        model=Salida
        fields=[
            "nombre",
            "categoria",
            "fechaSalida",
            "cantidad"
        ]