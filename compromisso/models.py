from django.db import models
from usuario import models as usuario
from contato import models as contato


# Create your models here.
class Compromisso(models.Model):
    idcompromisso = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=300)
    local = models.CharField(max_length=100)
    data = models.DateField()
    usuario = models.ForeignKey(usuario.Usuario, null=False, on_delete=models.RESTRICT)
    idcontato = models.ForeignKey(contato.Contato, null=False, on_delete=models.RESTRICT)
