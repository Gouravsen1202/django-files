from django.urls import path
from myapp2.views import django1,python1

urlpatterns = [
    path('dj', django1),
    path('py', python1),
    
]
