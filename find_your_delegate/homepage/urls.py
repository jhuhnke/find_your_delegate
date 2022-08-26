from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage-main'),
    path('about/', views.about, name='homepage-about'),
]
