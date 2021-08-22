from rest_framework import viewsets
from .authentication import UserAuthentication
from contato.models import Contato
from compromisso.models import Compromisso
from usuario.models import Usuario
from .serializers import ContatoSerializer, CompromissoSerializer, UsuarioSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


def validate_login(request):
    if request.method == 'POST':
        body_data = json.loads(request.body)
        username = body_data['username']
        password = body_data['password']
        try:
            user = Usuario.objects.get(username=username, senha=password)
            if user is not None:
                request.session['usuario_id'] = user.idusuario
                return JsonResponse({'success': '/'}, status=200)
            else:
                return JsonResponse({'error': 'Nome ou senha incorretos'}, status=400)
        except Usuario.DoesNotExist:
            return JsonResponse({'error': 'Nome ou senha incorretos'}, status=400)


class CompromissoViewSet(viewsets.ModelViewSet):
    serializer_class = CompromissoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['idcontato','data']

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Compromisso.objects.all()
        data_inicio = self.request.query_params.get('data_inicio')
        data_fim = self.request.query_params.get('data_fim')
        if (data_inicio is not None) and (data_fim is not None):
            queryset = Compromisso.objects.filter(data__range=[data_inicio, data_fim])
        return queryset


class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['idusuario', 'nome']

