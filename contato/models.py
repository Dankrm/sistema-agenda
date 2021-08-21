from django.db import models
from usuario import models as usuario


# Create your models here.
class Contato(models.Model):
    idcontato = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    fone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    idusuario = models.ForeignKey(usuario.Usuario, null=False, on_delete=models.RESTRICT)
