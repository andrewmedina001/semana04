
from django.contrib import admin
from django.urls import path, include

# Necesary for Swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
   openapi.Info(
      title="Aplicacion de Gestion de Tareas.",
      default_version='v1',
      description="API de gestion de tareas para empresas de servicios.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="henry.medina@tecsup.edu.pe"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('gestion/',include('gestion.urls')),
    path('autorizacion/',include('autorizacion.urls'))
    # Commentary line
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
appname='mainapp'