from django.db import models
from model_utils.models import TimeStampedModel, StatusField
from model_utils import Choices


class Shipment(TimeStampedModel):
    STATUS = Choices("pending", "shipped", "delivered")

    shipping_address = models.TextField("Shipping address")
    billing_address = models.TextField("Billing address")
    products_price = models.DecimalField(decimal_places=8, max_digits=10)
    delivery_code = models.IntegerField()
    status = StatusField(choices=STATUS)


class ShipmentDetails(TimeStampedModel):
    shipment = models.ForeignKey("shipments.Shipment", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField("Quantity")
    price_per_unit = models.DecimalField(
        "Price per unit", decimal_places=8, max_digits=10
    )
    price = models.DecimalField("Price", decimal_places=8, max_digits=10)
