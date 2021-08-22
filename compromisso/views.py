from django.shortcuts import render, get_object_or_404,reverse
from .models import Compromisso
from contato.models import Contato


def index(request):
    compromissos = Compromisso.objects.filter(usuario_id=request.session['usuario_id']).order_by('-data')
    contatos = Contato.objects.filter(idusuario=request.session['usuario_id'])
    return render(request, 'compromisso/index.html', {
        'compromissos': compromissos,
        'contatos': contatos
    })
