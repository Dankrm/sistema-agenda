from django.shortcuts import render, get_object_or_404,reverse
from .models import Contato
import requests

def index(request):
    contatos = Contato.objects.filter(idusuario=request.session['usuario_id']).order_by('-idcontato')
    return render(request, 'contato/index.html', {
        'contatos': contatos
    })
