
from django.urls import path
from myapp import views

urlpatterns = [
path('',views.home,name='home'),
path('contact/',views.reservetable,name='reservetabel'),
path('menu/',views.menu,name='menu'),
path('order/',views.order,name='order'),
path('Ragister/',views.ragister,name='Ragister'),
path('login/',views.login,name='login'),
path('deshbord/',views.deshbord,name='deshbord'),
path('track/',views.trackorder,name='track order'),
]
