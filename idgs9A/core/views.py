from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'core/home.html')
def peli(request):
    return render(request, 'core/peli.html')
def about(request):
    return render(request , 'core/about.html')