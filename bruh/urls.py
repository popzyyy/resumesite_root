from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('refresh/', views.refresh, name='refresh'),
    path('contact/', views.contact, name='contact'),
    path('experience/', views.experience, name='experience'),
    path('resume/', views.resume, name='resume'),


]
