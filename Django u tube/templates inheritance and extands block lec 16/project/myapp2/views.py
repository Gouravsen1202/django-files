from django.shortcuts import render

# Create your views here.
def django1(request):
    return render(request,'myapp2/django.html')
def python1(request):
    return render(request,'myapp2/python.html')
