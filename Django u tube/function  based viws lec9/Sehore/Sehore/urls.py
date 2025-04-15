"""
URL configuration for Sehore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from awadhpuri import views as awd1
from chanakpuri import views as cha1
urlpatterns = [
    path('admin/', admin.site.urls),
    path('myfun/', awd1.myfunction, name='myfunction'),
    path('myfun1/', awd1.myfunction1, name='myfun1'),
    path('myawad/',awd1.myawadh, name='myawadh'),
    path('math/',awd1.maths, name='mymath') ,
    path('chanak/', cha1.chanak,name='chanak'),
    
]


