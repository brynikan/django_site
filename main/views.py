from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"main/index.html")

def about(requests):
    return render(requests, "main/about.html")