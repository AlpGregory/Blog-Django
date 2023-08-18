from django.shortcuts import render


def home(request):
    return render(request, 'blog/index.html')


def generales(request):
    return render(request, 'blog/generales.html')


def programacion(request):
    return render(request, 'blog/programacion.html')


def tutoriales(request):
    return render(request, 'blog/tutoriales.html')


def tecnologia(request):
    return render(request, 'blog/tecnologia.html')


def videojuegos(request):
    return render(request, 'blog/videojuegos.html')
