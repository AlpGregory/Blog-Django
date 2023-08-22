from django.shortcuts import render
from blog.models import Post, Categoria


def home(request):
    posts = Post.objects.filter(estado=True)

    return render(request, 'blog/index.html', {'posts': posts})


def generales(request):
    posts = Post.objects.filter(estado=True, categoria=Categoria.objects.get(nombre='General'))

    return render(request, 'blog/generales.html', {'posts': posts})


def programacion(request):
    posts = Post.objects.filter(estado=True, categoria=Categoria.objects.get(nombre='Programacion'))

    return render(request, 'blog/programacion.html', {'posts': posts})


def tutoriales(request):
    posts = Post.objects.filter(estado=True, categoria=Categoria.objects.get(nombre='Tutoriales'))

    return render(request, 'blog/tutoriales.html', {'posts': posts})


def tecnologia(request):
    posts = Post.objects.filter(estado=True, categoria=Categoria.objects.get(nombre='Tecnologia'))

    return render(request, 'blog/tecnologia.html', {'posts': posts})


def videojuegos(request):
    posts = Post.objects.filter(estado=True, categoria=Categoria.objects.get(nombre='Video juegos'))

    return render(request, 'blog/videojuegos.html', {'posts': posts})
