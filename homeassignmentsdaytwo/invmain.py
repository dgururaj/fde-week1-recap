from fastapi import FastAPI
import importlib


get_invoices = importlib.import_module("homeassignmentsdaytwo.getinvoice").router
create_invoice = importlib.import_module("homeassignmentsdaytwo.create_inv").router
delete_invoice = importlib.import_module("homeassignmentsdaytwo.deleteinvoice").router
update_invoice = importlib.import_module("homeassignmentsdaytwo.updateinvoice").router

app = FastAPI()
app.include_router(get_invoices)
app.include_router(create_invoice)
app.include_router(delete_invoice)
app.include_router(update_invoice)