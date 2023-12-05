from django.urls import path
from. import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name='BASE'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('home', views.home, name='home'),
    path('createvent/', views.createvent, name='createvent'),
    path('eventlist/', views.eventlist, name='eventlist')

]