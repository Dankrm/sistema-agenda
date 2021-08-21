from django.urls import path, include
from rest_framework import routers

from .views import (
    CompromissoViewSet, ContatoViewSet, UsuarioViewSet, validate_login
)

api_router = routers.DefaultRouter()
api_router.register(r'compromisso', CompromissoViewSet, basename="compromisso")
api_router.register(r'contato', ContatoViewSet, basename="contato")
api_router.register(r'usuario', UsuarioViewSet, basename="usuario")


urlpatterns = [
    path('', include(api_router.urls)),
    path('login/', validate_login, name="login")
]

