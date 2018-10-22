from django.db import models

# Create your models here.

class Status(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Status'
    def __str__(self):
        return self.nome



class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField('Descrição', max_length=200)
    status = models.ForeignKey(Status,on_delete=models.CASCADE,null=True)
    data_criacao = models.DateField(auto_now=True)
    data_vencimento = models.DateField('Data de Vencimento',null=True)

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
    projetos = models.ForeignKey(Projeto, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.nome
