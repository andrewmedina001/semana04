from rest_framework import serializers
from .models import Tarea

class PruebaSerializer (serializers.Serializer):
    # definicion de columnas del serializer
    nombre=serializers.CharField(max_length=40)
    apellido=serializers.CharField(max_length=40)

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tarea
        # fields > sirve para indicar que atributos voy
            # a nevesitar / mostrar al cliente
        # en el caso de que se utilicen todos > __all__
        fields='__all__'