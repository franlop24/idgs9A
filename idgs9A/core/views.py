from django.shortcuts import render
from django.http import HttpResponse
from .models import Bar, Song, MagicTown

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def bars(request):
    bars = Bar.objects.all()
    return render(request, 'core/bars.html', {'bars':bars})

def music(request):
    songs = Song.objects.all()
    return render(request, 'core/music.html', {'songs':songs})

def towns(request):
    towns = MagicTown.objects.all()
    return render(request, 'core/towns.html', {'towns':towns})