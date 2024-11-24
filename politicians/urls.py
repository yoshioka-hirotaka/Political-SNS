from django.contrib import admin
from django.urls import path
from . import views

app_name = 'politicians'
urlpatterns = [
path('', views.index, name = 'index'),
path('<int:politician_id>/', views.detail, name = 'detail'),
]