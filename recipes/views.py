from django.http import HttpResponse
from django.shortcuts import render


def home(req):
    return HttpResponse('Home')


def contato(req):
    return HttpResponse('Contato')


def sobre(req):
    return HttpResponse('Sobre')
