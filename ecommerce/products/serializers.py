from rest_framework import serializers
from .models import Productos

class ProductoSerializer(serializers.Serializer):
    class Meta:
        model=Productos
        fields='__all__'