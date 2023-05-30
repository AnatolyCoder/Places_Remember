from django.urls import path
from map.views import MarkersMapView
from . import views


app_name = "map"

urlpatterns = [
    path("mapa/", MarkersMapView.as_view()),
    path("remember/", views.AddRemember.as_view(), name='add_remember')
]
