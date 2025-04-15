
from django.urls import path
from myapp.views import home, base

urlpatterns = [
    path('',home),
    path('base/',base)
    
]
