from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'videogames/home.html')

def about(request):
    return render(request, 'videogames/about.html')

def gameDetail(request):
    return render(request, 'videogames/gameDetail.html')