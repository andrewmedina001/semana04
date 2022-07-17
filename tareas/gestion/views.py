from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework.generics import ListAPIView
from .serializers import PruebaSerializer

@api_view(http_method_names=['GET','POST'])
def inicio(request:Request):
    print(request)
    return Response(data={
        'message':'Endpoint de un decorador'
    })

class PruebaView(ListAPIView):
    queryset=[{
        'nombre':'eduardo',
        'apellido':'de rivero'
    },{
        'nombre':'rozana',
        'apellido':'gonzales'
    }]
    serializer_class=PruebaSerializer