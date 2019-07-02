"""chave URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from core.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),
    path('mostrar_chaves', mostrar_chaves),
    path('informacoes_chave/<int:id>', informacoes_chave),
    path('mostrar_chaves_disponiveis/', mostrar_chaves_disponiveis),
    path('mostrar_chaves_indisponiveis/', mostrar_chaves_indisponiveis),
    path('pegar_chave/<int:id>', pegar_chave, name = 'pegar_chave'),
    path('devolver_chave/<int:id>', devolver_chave, name = 'devolver_chave'),
    path('historico_chave', historico_chave),

]
