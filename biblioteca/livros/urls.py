from django.urls import path
from . import views

urlpatterns = [
    path('livros/', views.index, name='index'),
    path('detalhes/<int:id>', views.livro_detalhes, name='livro_detalhe')
]