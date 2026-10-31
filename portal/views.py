from django.shortcuts import render
from .models import Conteudo, Menu

def home(request):
    menus = Menu.objects.filter(ativo=True)
    return render(request, 'portal/home.html', {'menus': menus})

def pagina_conteudo(request, slug):
    conteudo = Conteudo.objects.get(slug=slug, ativo=True)
    menus = Menu.objects.filter(ativo=True)
    return render(request, 'portal/conteudo.html', {'conteudo': conteudo, 'menus': menus})
# Create your views here.
