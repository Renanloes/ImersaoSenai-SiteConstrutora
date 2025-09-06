from django.db import models

class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    disponivel = models.BooleanField(default=True)

class Colaborador(models.Model):
    nome = models.CharField(max_length=45)
    cpf = models.CharField(max_length=45)

    def __str__(self):
        return self.nome