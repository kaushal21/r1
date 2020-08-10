from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about-us/', views.aboutUs, name='aboutUs'),
    path('services/', views.services, name='services')
]
