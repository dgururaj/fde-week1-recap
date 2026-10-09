from fastapi import APIRouter, HTTPException
from homeassignmentsdaytwo.invmodel import invoice
from homeassignmentsdaytwo.getinvoice import JSON_FILE, load_invoices
import json

router = APIRouter()


@router.post("/invoices", status_code=201)
def create_invoice(new_invoice: invoice):
	invoices = load_invoices()

	if any(existing["invoice_id"] == new_invoice.invoice_id for existing in invoices):
		raise HTTPException(status_code=409, detail="Invoice already exists")

	invoices.append(new_invoice.model_dump())

	with open(JSON_FILE, "w", encoding="utf-8") as file:
		json.dump(invoices, file, indent=2)

	return {
		"message": "Invoice is created",
		"invoice": new_invoice,
	}