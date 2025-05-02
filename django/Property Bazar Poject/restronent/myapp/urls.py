
from django.urls import path
from myapp import views

urlpatterns = [
path('',views.home,name='home'),
path('',views.home1,name='home'),
path('menu/',views.menu,name='menu'), #selling
path('order/',views.order,name='order'),#purchase
path('menu/',views.menu1,name='menu'), #selling
path('order/',views.order1,name='order'),#purchase
path('Ragister/',views.ragister,name='Ragister'),
path('login/',views.login,name='login'),
path('deshbord/',views.deshbord,name='deshbord'),
path('track/',views.trackorder,name='track order'),
path('track/',views.trackorder1,name='track order'),
]
