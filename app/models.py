from django.db import models

# Create your models here.
class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    tarefas = models.ForeignKey(Tarefa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    senha = models.CharField(max_length=200)
    projetos = models.ForeignKey(Projeto, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.nome
    