from django.contrib import admin
from .models import Usuario, Status
from .models import Projeto
from .models import Tarefa
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Projeto)
admin.site.register(Tarefa)
admin.site.register(Status)