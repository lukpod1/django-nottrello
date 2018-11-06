"""nottrello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app.views import home, entrar, cadastrar, usuarioLogado, editarTarefa, excluirTarefa, excluirProjeto,listarTarefaProjeto, logout, editarPerfil, editarProjeto, concluirProjeto
from nottrello import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('home/', home),
    path('usuario/entrar', entrar),
    path('usuario/cadastrar', cadastrar),
    path('usuario/logado/<int:pk_usuario>', usuarioLogado, name='usuarioLogado'),
    path('usuario/perfil/<int:pk_usuario>', editarPerfil),
    path('<int:pk_usuario>/projeto/<int:pk_projeto>', listarTarefaProjeto),
    path('projeto/excluir/<int:pk>', excluirProjeto),
    path('projeto/editar/<int:pk>', editarProjeto),
    path('projeto/concluir/<int:pk>', concluirProjeto),
    path('tarefa/editar/<int:pk>', editarTarefa),
    path('tarefa/excluir/<int:pk>', excluirTarefa),
    
    path('usuario/logout', logout)


]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
