
from django.urls import path
from mycourse.views import course,fastapi

urlpatterns = [
    path('course/', course),
    path('api/', fastapi)
]
