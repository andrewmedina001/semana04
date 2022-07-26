from ast import Is
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework.generics import ListAPIView,ListCreateAPIView
from .serializers import PruebaSerializer, TareaSerializer

from rest_framework.permissions import IsAuthenticated

from .models import Tarea

@api_view(http_method_names=['GET','POST'])
def inicio(request:Request):
    print(request)
    return Response(data={
        'message':'Endpoint de un decorador'
    })

class PruebaView(ListAPIView):
    # retorna el resultado de la interaccion con el ORM y
    # se usa para los metodos de devolucion (GET)
    queryset=[{
        'nombre':'eduardo',
        'apellido':'de rivero'
    },{
        'nombre':'rozana',
        'apellido':'gonzales'
    }]

    # serielizador es un DTO (Data Transfer Object)
    # serializer_class > convierte la info que llega desde
        #  el cliente y tambien la info que retornaremos
        # hacia el cliente
    serializer_class=PruebaSerializer


# ListAPIView > GET
# ListCREATEAPIView > GET , POST
class TareasView(ListCreateAPIView):
    # equivalent > SELECT * FROM tareas;
    # objeets > base maanager
    queryset=Tarea.objects.all()
    serializer_class=TareaSerializer

    # 
    permission_classes=[IsAuthenticated]

    def get(self,request:Request):
        
        # manda a llamar a la ejecucion de nuestro queryset
            #retorna todas las tareas sin verificar si son de el 
        # tareas=self.get_queryset() 
        usuarioId=request.user.id

        # Equivalent to SELECT * FROM tareas WHERE usuarioId = ... ;
        tareas=Tarea.objects.filter(usuarioId=usuarioId).all()

        tareasSerielizadas=self.serializer_class(instance=tareas,many=True)

        return Response(data={
            'message':'Las tareas son:',
            'content':tareasSerielizadas.data
        })
    def post(self,request:Request):
        body=request.data
        print(request.user.nombre)
        # Modificando el body entrante y le agrego el ID del usuario que actualmente esta
            # haciendo la peticion
        body['usuarioId']=request.user.id
        instanciaSerializador=self.serializer_class(data=body)
        validacion=instanciaSerializador.is_valid(raise_exception=True)
        # Hola
        if validacion==True:
            instanciaSerializador.save()
            return Response(data=instanciaSerializador.data,status=201)