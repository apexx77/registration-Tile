from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('registrationpage', views.registrationpage, name='registrationpage'),
    path('final',views.final, name='final'),
    path('home',views.home, name='home')


]