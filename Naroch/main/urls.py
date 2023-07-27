from django.urls import path
from . import views
from admin_for_staff import views as admin_for_staff

urlpatterns = [
    path('', views.index, name="home"),
    path('price/', views.booking, name="booking"),
    path('calendar/', views.calendar, name="calendar"),
]
