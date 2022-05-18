from django.contrib import admin
from .models import Shipment, ShipmentDetails


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    pass


@admin.register(ShipmentDetails)
class ShipmentDetailsAdmin(admin.ModelAdmin):
    pass
