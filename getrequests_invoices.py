#getrequests_invoices.py implements a FastAPI server that retrieves invoice data from an external API and provides endpoints to access the data.
from fastapi import APIRouter
from typing import List
from data_store import invoices


router = APIRouter()



@router.get("/")
def home():
    return {"message": "FastAPI server is running"}

@router.get("/invoices")
def get_invoices():
    return invoices 


@router.get("/invoices/{invoice_id}")
def get_invoice(invoice_id: int):
    for invoice in invoices:
        if invoice["id"] == invoice_id:
            return invoice

    return {"error": "Invoice not found"}   