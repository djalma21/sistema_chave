from django.db import models

# Create your models here.



class Chave(models.Model):
    nome = models.CharField(max_length=100)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    nome = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    chave = models.ForeignKey(Chave, on_delete=models.CASCADE)
    horas_pegou = models.TimeField()

    def __str__(self):
        return self.nome

class Devolver(models.Model):
    nome = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    chave = models.ForeignKey(Chave, on_delete=models.CASCADE)
    horas_devolveu = models.TimeField()

    def __str__(self):
        return self.nome



