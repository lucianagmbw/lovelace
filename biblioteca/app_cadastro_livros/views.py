from django.shortcuts import render,redirect
from .models import Livros
from .forms import BuscaLivroForm,BuscaAutorForm


def home(request):
    return render(request,'livros/home.html')

"""""
def listagem(request):
    novo_livro = Livros()
    novo_livro.titulo = request.POST.get('titulo')
    novo_livro.autor = request.POST.get('autor')
    novo_livro.quantidade = request.POST.get('quantidade')
     
    novo_livro.save()
   
    diclivros = {
        'diclivros' : Livros.objects.all()
    }
    
    return render(request,'livros/listagem.html', diclivros)

"""

def listagem(request):
    if request.method == 'POST':
        novo_livro = Livros()
        novo_livro.titulo = request.POST.get('titulo')
        novo_livro.autor = request.POST.get('autor')
        quantidade = int(request.POST.get('quantidade', 0))  # Converte para inteiro
       
        if quantidade > 0:
            novo_livro.quantidade = quantidade
            novo_livro.save()
        else:
            # Caso a quantidade seja menor ou igual a zero, você pode retornar um erro ou redirecionar para uma página de erro.
            return render(request, 'livros/erro_quantidade.html')

    diclivros = {
        'diclivros': Livros.objects.all()
    }
    
    return render(request, 'livros/listagem.html', diclivros)


def buscar_livro(request):
    if request.method == 'POST':
        form = BuscaLivroForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            livros = Livros.objects.filter(titulo__icontains=titulo)
            return render(request, 'livros/listagem.html', {'diclivros': livros})
    else:
        form = BuscaLivroForm()
    
    return render(request, 'livros/buscar.html', {'form': form})


def buscar_autor(request):
    if request.method == 'POST':
        form = BuscaAutorForm(request.POST)
        if form.is_valid():
            autor = form.cleaned_data['autor']
            livros = Livros.objects.filter(autor__icontains=autor)
            return render(request, 'livros/listagem.html', {'diclivros': livros})
    else:
        form = BuscaAutorForm()
    
    return render(request, 'livros/buscar_autor.html', {'form': form})