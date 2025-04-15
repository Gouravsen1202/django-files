
from django.urls import path
from myapp2.views import python,django

urlpatterns = [
    path('py/',python),
    path('dj/',django)
    
]
