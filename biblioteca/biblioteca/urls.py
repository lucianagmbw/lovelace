
from django.contrib import admin
from django.urls import path
from app_cadastro_livros import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('listagem/', views.listagem,name='listagem_livros'),
    path('buscar/', views.buscar_livro, name='buscar_livro'),
    path('buscar-autor/', views.buscar_autor, name='buscar_autor'),  
    
]
