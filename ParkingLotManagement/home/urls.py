from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.index, name='home'),
    path('login', views.loginuser, name='login'),
    path('logout', views.logoutuser, name='logout'),
    path('search', views.search, name='search'),
    path('display', views.display, name='display'),
    path('details', views.details, name='details')
    
]
