from django.urls import path
from . import views

urlpatterns = [
    path("farmers/",views.farmers,name="farmers"),
    path("farmer/<str:pk>/",views.farmer,name="farmer"),
    path("createFarmer/",views.createFarmer,name="createfarmer"),
    path("createVenture/",views.createVenture,name="createventure"),
    path("createFarm/",views.createFarm,name="createfarm"),
    path("",views.ventures,name="ventures"),
    path("farms/",views.farms,name="farms"),
    path("updateFarmer/<str:pk>/",views.updateFarmer,name="updatefarmer"),
    path("deleteObject/<str:pk>/",views.deleteObject,name ="deletefarmer")
    ]
