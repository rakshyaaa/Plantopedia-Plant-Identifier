from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = "applicationPredict"

urlpatterns = [
    path('', views.application, name='predict'),
    # path('predictImage', views.predictImage, name='predictImage')
]

urlpatterns +=  staticfiles_urlpatterns()