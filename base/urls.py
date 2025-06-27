from django.urls import path
from .views import *

urlpatterns = [
    path("navbar/", navigation, name="nav"),
    path("", home, name="home"),
    path("detail/<int:detail_id>/", detail_clothes, name="detail"),
    path('filter/<str:jinsi>/', kiyimlar_view, name='jins_filter'),
    path('skidkalar/', skidkali_kiyimlar_view, name='skidkali_kiyimlar'),
    path("yosh/<str:yosh>/", yosh_boyicha, name="yosh_boyicha"),
    path("register/", register, name="register"),
]