from django.shortcuts import render
from django.http import HttpResponse
from .models import Characters


def home(request):
    posts = Characters.objects.all()
    return render(request, 'home.html', {'posts': posts})

def characters(request):
    posts = Characters.objects.all()
    return render(request, 'characters.html', {'posts': posts})