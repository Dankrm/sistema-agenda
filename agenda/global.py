
from django.shortcuts import render
from usuario import models


def is_usuario_logado(request):
    response = False
    try:
        if request.session['usuario_id'] is not None:
            response = True
    except:
        pass
    return {'is_logado': response}


def get_user(request):
    user = False
    try:
        if request.session['usuario_id'] is not None:
            user = models.Usuario.objects.get(idusuario=request.session['usuario_id'])
    except:
        pass
    return {'user': user}
