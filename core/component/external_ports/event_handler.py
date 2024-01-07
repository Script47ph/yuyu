from core.component.base.event_handler import EventHandler
from core.component.external_ports.invoice_handler import ExternalPortInvoiceHandler


class ExternalPortEventHandler(EventHandler):
    def handle(self, event_type, raw_payload):
        if event_type == 'externalport.create.end':
            tenant_id = raw_payload['port']['tenant_id']
            invoice = self.get_tenant_progress_invoice(tenant_id)
            self.handle_create(invoice, event_type, raw_payload)

        if event_type == 'externalport.delete.end':
            tenant_id = raw_payload['port']['tenant_id']
            invoice = self.get_tenant_progress_invoice(tenant_id)
            self.handle_delete(invoice, event_type, raw_payload)

    def clean_payload(self, event_type, raw_payload):
        payload = {
            "port_id": raw_payload['port']['id'],
            "ip": raw_payload['port']['ip_address'],
        }

        return payload
