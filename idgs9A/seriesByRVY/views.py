from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'seriesByRVY/home.html')

def seriesList(request):
    return render(request, 'seriesByRVY/seriesList.html')

def detail(request):
    return render(request, 'seriesByRVY/detail.html')
