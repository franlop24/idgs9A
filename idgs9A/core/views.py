from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def bars(request):
    return render(request, 'core/bars.html')

def music(request):
    return render(request, 'core/music.html')

def towns(request):
    return render(request, 'core/towns.html')