
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('', views.add_address, name="add_address"),
]
