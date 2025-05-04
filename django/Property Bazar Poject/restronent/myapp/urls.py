
from django.urls import path
from myapp import views

urlpatterns = [
path('',views.home,name='home'),
path('menu/',views.menu,name='menu'), #selling
path('order/',views.order,name='order'),#purchase
path('Ragister/',views.ragister,name='Ragister'),
path('login/',views.login,name='login'),
path('deshbord/',views.deshbord,name='deshbord'),
path('logout/', views.logout, name='logout'),
path('track/',views.trackorder,name='track order'),
path('Service/',views.Service,name='Service'),


path('home/<int:pk>',views.home1,name='home1'),
path('menu/<int:pk>',views.menu1,name='menu1'),
path('order/<int:pk>',views.order1,name='order1'),
path('track/<int:pk>',views.trackorder1,name='track order1'),
path('Service/<int:pk>',views.Service1,name='Service1')


]
