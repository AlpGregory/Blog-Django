from django.urls import path
from blog.views import home, detalle_post, generales, programacion, videojuegos, tecnologia, tutoriales


urlpatterns = [
    path('', home, name='index'),
    path('generales/', generales, name='generales'),
    path('programacion/', programacion, name='programacion'),
    path('videojuegos/', videojuegos, name='videojuegos'),
    path('tecnologia/', tecnologia, name='tecnologia'),
    path('tutoriales/', tutoriales, name='tutoriales'),
    path('<slug:slug>/', detalle_post, name='detalle_post'),
]
