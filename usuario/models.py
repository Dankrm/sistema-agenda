from django.db import models


# Create your models here.
class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    senha = models.CharField(max_length=8)
