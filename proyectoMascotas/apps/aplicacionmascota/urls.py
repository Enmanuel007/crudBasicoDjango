from django.conf.urls import url
from .views import *
from django.db import models




urlpatterns = [

    url(r'^$', home, name="Index"),
    url(r'^crear_mascota/',crearMascota,name="nueva_Mascota"),
]