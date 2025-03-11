from django.shortcuts import render 
from .models import Livro

def index(request):
    
    livros = Livro.objects.all()
    
    return render(request, 'pages/index.html', {'livros':livros})


def livro_detalhes(request, id):
    
    livro = Livro.objects.get(id=id)
        
    return render(request, 'pages/livro_detalhes/index.html', {'livro':livro})