from django.urls import path
from .views import PruebaView, inicio, PruebaView

# Seran todas las rutas que puede ser accedidas a esta aplicacion
urlpatterns=[
    path('inicio',inicio),
    path('prueba',PruebaView.as_view())
]