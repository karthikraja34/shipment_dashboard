from django.conf import settings
from django.views import generic

from products.models import Product
from shipments.models import Shipment, ShipmentDetail


class ShipmentListView(generic.ListView):
    template_name = "list.html"
    model = Shipment
    context_object_name = "shipments"
    queryset = Shipment.objects.all().select_related("user", "user__company")


class ShipmentDetailView(generic.DetailView):
    template_name = "detail.html"
    model = Shipment
    pk_url_kwarg = "pk"
    queryset = Shipment.objects.all().select_related("user", "user__company")

    def get_context_data(self, **kwargs):
        context = super(ShipmentDetailView, self).get_context_data(**kwargs)
        shipment = self.get_object()
        context["products"] = self.get_products(shipment)
        context["config"] = self.get_config(shipment)
        return context

    def get_products(self, shipment):
        product_ids = ShipmentDetail.objects.filter(shipment=shipment).values_list(
            "product_id", flat=True
        )
        return Product.objects.filter(id__in=product_ids)

    def get_config(self, shipment):
        self.get_products(shipment)
        config = settings.DASHBOARD_SETTINGS.get(
            shipment.status, settings.DASHBOARD_SETTINGS["default"]
        )
        config["product_chart"] = {
            "labels": list(
                shipment.shipment_details.values_list("product__name", flat=True)
            ),
            "data": list(shipment.shipment_details.values_list("quantity", flat=True)),
        }
        return config
