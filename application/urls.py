from django.urls import path
from . import views

app_name = "applicationPredict"

urlpatterns = [
    path('', views.application, name='predict'),
    # path('predictImage', views.predictImage, name='predictImage')
]


