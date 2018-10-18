from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    senha = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome
    