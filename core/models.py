from django.db import models
from django.contrib.auth.models import User


class Chave(models.Model):
    nome = models.CharField(max_length=100)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    chave = models.ForeignKey(Chave, on_delete=models.CASCADE)
    horas_pegou = models.TimeField()

    def __str__(self):
        return f' {self.user} - {self.chave} - {self.horas_pegou} '
class Devolver(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chave = models.ForeignKey(Chave, on_delete=models.CASCADE)
    horas_devolveu = models.TimeField()

    def __str__(self):
        return f'{self.user} - {self.chave} - {self.horas_devolveu}'


