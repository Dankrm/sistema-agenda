
from rest_framework import serializers
from contato import models as contato
from compromisso import models as compromisso
from usuario import models as usuario


class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = contato.Contato
        fields = '__all__'


class CompromissoSerializer(serializers.ModelSerializer):
    class Meta:
        model = compromisso.Compromisso
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario.Usuario
        fields = '__all__'
