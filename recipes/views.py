from django.http import HttpResponse
from django.shortcuts import render


def home(req):
    return render(req, 'recipes/home.html')


def contato(req):
    return HttpResponse('Contato')


def sobre(req):
    return HttpResponse('Sobre')
