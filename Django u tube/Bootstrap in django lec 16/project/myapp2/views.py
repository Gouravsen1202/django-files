from django.shortcuts import render

def python(request):
    return render(request,'myapp2/python.html')


def django(request):
    return render(request,'myapp2/django.html')



