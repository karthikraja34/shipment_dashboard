from django.urls import path

from . import views

urlpatterns = [
    path("", views.ShipmentListView.as_view(), name="index"),
    path("<int:pk>/", views.ShipmentDetailView.as_view(), name="detail"),
]
