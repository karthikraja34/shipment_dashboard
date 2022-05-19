from django.urls import path

from . import views

urlpatterns = [
    path("", views.ShipmentListView.as_view(), name="index"),
]
