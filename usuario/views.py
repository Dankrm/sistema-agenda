from django.shortcuts import render, reverse, HttpResponseRedirect
from .models import Usuario


def index(request):
    usuarios = Usuario.objects.all().order_by('-idusuario')
    return render(request, 'usuario/index.html', {
        'usuarios': usuarios
    })


def logout(request):
    request.session['usuario_id'] = None
    return HttpResponseRedirect('/')
