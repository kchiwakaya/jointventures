from django.urls import path
from . import views

urlpatterns = [
    path("farmers/",views.farmers,name="farmers"),
    path("farmer/<str:pk>/",views.farmer,name="farmer"),
    path("createFarmer/",views.createFarmer,name="createfarmer"),
    path("createVenture/",views.createVenture,name="createventure"),
    path("createFarm/",views.createFarm,name="createfarm"),
    path("ventures/",views.ventures,name="ventures"),]
