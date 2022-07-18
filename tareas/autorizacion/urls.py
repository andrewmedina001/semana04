from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns=[
    # token que brindara
    path('login',TokenObtainPairView.as_view())
]