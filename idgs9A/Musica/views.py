from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("Inicio")

def cancion(request):
    return HttpResponse("Cancion")

def album(request):
    return HttpResponse("Album")

def store(request):
    return HttpResponse("Visítanos")

def contact(request):
    return HttpResponse("Contacto")

def blog(request):
    return HttpResponse("Blog")

def sample(request):
    return HttpResponse("Sample")

