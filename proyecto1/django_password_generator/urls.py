from django.urls import path
from generator import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate-password', views.generatedPassword, name='password'),
    path('about', views.about, name='about'),
]
