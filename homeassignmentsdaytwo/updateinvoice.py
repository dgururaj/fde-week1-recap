import json

from fastapi import APIRouter, HTTPException

from homeassignmentsdaytwo.getinvoice import JSON_FILE, load_invoices
from homeassignmentsdaytwo.invmodel import invoice

router = APIRouter()


@router.put("/invoices/{invoice_id}")
def update_invoice(invoice_id: str, updated_invoice: invoice):
    if updated_invoice.invoice_id != invoice_id:
        raise HTTPException(
            status_code=400,
            detail="Invoice ID in URL must match invoice ID in request body",
        )

    invoices = load_invoices()

    for index, existing_invoice in enumerate(invoices):
        if existing_invoice["invoice_id"] == invoice_id:
            invoices[index] = updated_invoice.model_dump()

            with open(JSON_FILE, "w", encoding="utf-8") as file:
                json.dump(invoices, file, indent=2)

            return {
                "message": "Invoice is updated",
                "invoice": updated_invoice,
            }

    raise HTTPException(status_code=404, detail="Invoice not found")