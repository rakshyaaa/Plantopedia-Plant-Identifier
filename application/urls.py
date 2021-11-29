from django.urls import path
from . import views

urlpatterns = [
    path('', views.application, name='application'),
    path('predictImage', views.predictImage, name='predictImage')
]


