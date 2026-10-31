from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('conteudo/<slug:slug>/', views.pagina_conteudo, name='pagina_conteudo'),
    ]
