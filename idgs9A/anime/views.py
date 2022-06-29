from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'anime/home.html')

def animes(request):
    return render(request, 'anime/animes.html')