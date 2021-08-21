from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from home import views as home


def index(request):
    return render(request, "login/index.html")




