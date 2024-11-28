from django.urls import path

from . import views

app_name = 'facerec'
urlpatterns = [
    path("<int:election_id>/", views.facerec, name="facerec"),
    path("<int:election_id>/shoot/", views.shoot, name="shoot"),
    path("<int:election_id>/upload/", views.upload, name="upload"),
    path("<int:election_id>/reco/", views.reco, name="reco"),
    path("<int:election_id>/capture/", views.capture, name="capture"),
]