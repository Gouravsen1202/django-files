from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def chanak(request):
    return HttpResponse("<h1>this is chanak<h1/>")