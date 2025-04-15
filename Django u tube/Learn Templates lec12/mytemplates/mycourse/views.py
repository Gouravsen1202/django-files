from django.shortcuts import render


# Create your views here.
def course(request):
    return render(request,'mycourse/django.html')
def fastapi(request):
    return render(request,'mycourse/fastapi.html')
