from fastapi import FastAPI
import importlib

create_invoice = importlib.import_module("createinvoice").router
get_invoices = importlib.import_module("getrequests_invoices").router

app = FastAPI()
app.include_router(create_invoice)
app.include_router(get_invoices)