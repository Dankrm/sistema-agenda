from django.shortcuts import render, get_object_or_404,reverse
from .models import Usuario


def index(request):
    usuarios = Usuario.objects.all().order_by('-idusuario')
    return render(request, 'usuario/index.html', {
        'usuarios': usuarios
    })
