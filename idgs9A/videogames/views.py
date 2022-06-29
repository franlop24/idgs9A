from django.shortcuts import render
from django.http import HttpResponse
from .models import Videogames

# Create your views here.
def home(request):
    videojuegos = Videogames.objects.all()
    return render(request, 'videogames/home.html', {'videojuegos' :videojuegos})

def about(request):
    return render(request, 'videogames/about.html')

def gameDetail(request):
    return render(request, 'videogames/gameDetail.html')

def games(request):
    videojuegos = Videogames.objects.all()
    return render(request, 'videogames/games.html', {'videojuegos' :videojuegos})