from django.shortcuts import render, redirect
from django.http import HttpResponse
from anime.models import Anime

# Create your views here.
def home(request):
    return render(request, 'anime/home.html')



def registrar_anime(request):
    anime = Anime(
        nombre_anime = 'Don’t Toy with Me, Miss Nagatoro',
        descripcion_anime = 'Basado en el manga web de Nanashi que se publicó en 2017, este anime se centra en la vida de Naoto Hachioji, un tímido estudiante de preparatoria que prefiere evitar a la gente y dibujar. Sin embargo, un día se encuentra con Hayase Nagatoro, una chica que al parecer disfruta de molestarlo.',
        genero_anime = 'N/A',
        imagen_anime = 'nagatoro.jpg'
    )
    
    anime.save()

    return redirect('../animes')

def listaAnimes(request):

    lista_animes = Anime.objects.all()


    return render(request, 'anime/animes.html', {
        'anime': lista_animes
    })

def borrar_anime(request, id):
    anime = Anime.objects.get(pk=id)
    anime.delete()

    return redirect('../animes')