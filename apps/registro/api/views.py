from apps.registro.models import Material 
from apps.registro.api.serializers import MaterialSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MaterialViews(APIView):
    def get (self,request):
        serializer= MaterialSerializer(Material.objects.all(),many=True)
        return Response (status=status.HTTP_200_OK,data=serializer.data)
    
    def post(self,request):
        serializer=MaterialSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return self.get(request)