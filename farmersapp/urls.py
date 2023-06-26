from django.urls import path
from . import views

urlpatterns = [
    path("farmers/",views.farmers,name="farmers"),
    path("farmer/<str:pk>/",views.farmer,name="farmer"),
    path("createFarmer/",views.createFarmer,name="createfarmer"),
    path("createVenture/<str:pk>/",views.createVenture,name="createventure"),
    path("createFarm/<str:pk>/",views.createFarm,name="createfarm"),
    path("",views.ventures,name="ventures"),
    path("farms/",views.farms,name="farms"),
    path("updateFarmer/<str:pk>/",views.updateFarmer,name="updatefarmer"),
    path("deleteObject/<str:pk>/",views.deleteObject,name ="deletefarmer"),
    path("details/<str:pk>/",views.details,name ="details"),
    path("register/",views.register,name ="register"),
    path("logout/", views.logout_user, name="logout"),
    ]
