from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def cse(request):
    return HttpResponse('Welcome to cse page')

def etc(request):
    return HttpResponse('Welcome to etc page')

def mech(request):
    return HttpResponse('Welcome to mech page')

def civil(request):
    return HttpResponse('Welcome to civil page')