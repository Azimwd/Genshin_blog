from django.shortcuts import render
from django.http import HttpResponse
from .models import Charapters


def home(request):
    posts = Charapters.objects.all()
    return render(request, 'home.html', {'posts': posts})

def charapters(request):
    posts = Charapters.objects.all()
    return render(request, 'charapters.html', {'posts': posts})