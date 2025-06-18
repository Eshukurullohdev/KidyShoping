from django.urls import path
from .views import *

urlpatterns = [
    path("navbar/", navigation, name="nav"),
    path("", home, name="home"),
    path("detail/", detail_clothes, name="detail")
]