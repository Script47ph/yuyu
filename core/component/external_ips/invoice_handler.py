from core.exception import PriceNotFound
from core.models import ExternalIpsPrice, InvoiceExternalIp, PriceMixin
from core.component.base.invoice_handler import InvoiceHandler


class ExternalIpInvoiceHandler(InvoiceHandler):
    INVOICE_CLASS = InvoiceExternalPort
    KEY_FIELD = "port_id"
    PRICE_DEPENDENCY_FIELDS = []
    INFORMATIVE_FIELDS = ["ip"]

    def get_price(self, payload) -> PriceMixin:
        price = ExternalIpsPrice.objects.first()

        if price is None:
            raise PriceNotFound(identifier='external ip')

        return price

