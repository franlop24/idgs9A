from django.shortcuts import render
from django.http import HttpResponse
from .models import Bar, Song, MagicTown

# Create your views here.
def home(request):
    return render(request, 'equipoJWN/home.html')

def bars(request):
    bars = Bar.objects.all()
    return render(request, 'equipoJWN/bars.html', {'bars':bars})

def songs(request):
    songs = Song.objects.all()
    return render(request, 'equipoJWN/music.html', {'songs':songs})

def towns(request):
    towns = MagicTown.objects.all()
    return render(request, 'equipoJWN/towns.html', {'towns':towns})