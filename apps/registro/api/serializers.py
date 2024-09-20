from apps.registro.models import Material
from rest_framework.serializers import ModelSerializer

class MaterialSerializer(ModelSerializer):
    class Meta:
        model=Material
        fields=[
            "nombre",
            "categoria",
            "fechaIngreso",
            "cantidad"
        ]