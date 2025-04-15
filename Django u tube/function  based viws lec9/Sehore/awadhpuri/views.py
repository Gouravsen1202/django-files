from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myfunction(request):
    return HttpResponse ("hellow django")

def myfunction1(request):
    return HttpResponse ("lec 1")

def myawadh(request):
    return HttpResponse("<h1>welcome <br>awadthpuri,a<h1/>")

def maths(resuest):
    a=7
    b=9
    c=a+b
    return HttpResponse(c)