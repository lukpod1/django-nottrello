from django.db import models


# Create your models here.

def uploac_location(instance, filename):
    return "%s/%s" %(instance, filename)


class Status(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Status'

    def __str__(self):
        return self.nome


class Usuario(models.Model):
    nomeCompleto = models.CharField('Nome Completo', max_length=50)
    nomeUsuario= models.CharField('Usuario', max_length=50)
    email = models.EmailField(max_length=50)
    senha = models.CharField(max_length=50)
    avatar = models.ImageField("Foto do perfil", upload_to=uploac_location, blank=True)

    def __str__(self):
        return self.nomeUsuario


class Pergunta(models.Model):
    titulo = models.CharField('Título', max_length=200)
    detalhesPergunta = models.CharField('Detalhes', max_length=5000)
    data_criacao = models.DateField("Criação", auto_now=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Resposta(models.Model):
    conteudo = models.CharField( max_length=5000)
    data_criacao = models.DateTimeField("Criação", auto_now=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, null=True, blank=True)
    like = models.IntegerField(blank=True, null=True, default=0)
    deslike = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.conteudo


class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    data_vencimento = models.DateField('Concluir até:', null=True)
    detalhes = models.CharField('Descrição', max_length=200, default="", blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=True, null=True,blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=True, null=True,blank=True)
    

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField('Descrição', max_length=200)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=True, null=True,blank=True)
    data_criacao = models.DateField(auto_now=True)
    data_vencimento = models.DateField('Data de Vencimento', null=True)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.nome