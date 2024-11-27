from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("facerec/", views.facerec, name="facerec"),
    path("facerec/shoot/", views.shoot, name="shoot"),
    path("facerec/upload/", views.upload, name="upload"),
    path("facerec/reco/", views.reco, name="reco"),
]