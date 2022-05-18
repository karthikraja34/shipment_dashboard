import random

from django.db import models
from model_utils.models import TimeStampedModel, StatusField
from model_utils import Choices


class Shipment(TimeStampedModel):
    STATUS = Choices("pending", "shipped", "delivered")

    shipping_address = models.TextField("Shipping address")
    billing_address = models.TextField("Billing address")
    products_price = models.DecimalField(decimal_places=8, max_digits=16)
    delivery_code = models.IntegerField()
    status = StatusField(choices=STATUS)
    user = models.ForeignKey("users.User", null=True, on_delete=models.SET_NULL)
    shipped_date = models.DateTimeField(null=True, blank=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    reference_id = models.CharField("Reference ID", max_length=20)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.reference_id = (
                self.user.company.name[:4].upper()
                + str(random.randint(1000, 99999))
                + str(self.user.pk)
                + str(random.randint(1000, 99999))
            )
        super(Shipment, self).save(*args, **kwargs)


class ShipmentDetail(TimeStampedModel):
    shipment = models.ForeignKey("shipments.Shipment", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField("Quantity")
    price_per_unit = models.DecimalField(
        "Price per unit", decimal_places=8, max_digits=16
    )
    price = models.DecimalField("Price", decimal_places=8, max_digits=16)
