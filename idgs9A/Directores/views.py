from django.shortcuts import render
from django.shortcuts import render, HttpResponse

def home(request):
        return render(request, "infoDir/home.html")
def peli(request):
        return render(request, "infoDir/peli.html")

