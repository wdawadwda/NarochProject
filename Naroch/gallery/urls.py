from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo_galery, name="galery"),
    path('outside', views.photo_outside, name="outside"),
    path('first_house', views.photo_first_house, name="first_house"),
    path('second_house', views.photo_second_house, name="second_house"),
    path('bath_house', views.photo_bath_house, name="bath_house"),
    path('area', views.photo_area, name="area"),
]