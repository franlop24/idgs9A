<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "musica/home.html")

def album(request):
    return render(request, "musica/albums.html")

def store(request):
    return HttpResponse("Visítanos")

def contact(request):
        return render(request, "musica/about.html")

def blog(request):
    return HttpResponse("Blog")

def sample(request):
    return HttpResponse("Sample")

=======
from django.shortcuts import render
>>>>>>> DCM
