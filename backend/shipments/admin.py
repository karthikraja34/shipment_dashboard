from django.contrib import admin
from .models import Shipment, ShipmentDetail


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    pass


@admin.register(ShipmentDetail)
class ShipmentDetailAdmin(admin.ModelAdmin):
    pass
