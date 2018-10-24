from django.db import models


# Create your models here.

class Status(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Status'

    def __str__(self):
        return self.nome


class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    senha = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="static/app/imgs/uploads/", blank=True)

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    data_vencimento = models.DateField('Concluir até:', null=True)
    detalhes = models.CharField('Descrição', max_length=200, default="", blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=True)

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField('Descrição', max_length=200)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=True, null=True,blank=True)
    data_criacao = models.DateField(auto_now=True)
    data_vencimento = models.DateField('Data de Vencimento', null=True)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, default=True, null=True,blank=True)


    def __str__(self):
        return self.nome