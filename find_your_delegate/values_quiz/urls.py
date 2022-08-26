from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='values-quiz'),
    path('results/', views.results, name='values-result'),
]