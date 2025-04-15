from django.urls import path
from course.views import course,Student

urlpatterns = [
   path("course/",course),
   path("Student/",Student)
]