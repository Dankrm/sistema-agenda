from django.urls import include, path
from rest_framework import routers
from .views import index, logout

urlpatterns = [
    path('', index, name='index'),
    path('logout/', logout, name='logout'),
]
