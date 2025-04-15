from django.shortcuts import render
from django.http import HttpResponse

def app1(request):
    return HttpResponse("this is app 1 go to app 2")

