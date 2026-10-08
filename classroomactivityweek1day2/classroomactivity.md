Activity1:
Create a new Employee - Post Call
Start as a uvicorn app & test it with postman


Activity2:
a. Create a models.py (Pydantic)
from pydantic import BaseModel


class Invoice(BaseModel):
id: int
amount: float
status: str


b. Create a data_store.py (In-Memory Data Store) 


invoices = [
{"id": 1, "amount": 100.0, "status": "paid"},
{"id": 2, "amount": 200.0, "status": "unpaid"},
{"id": 3, "amount": 150.0, "status": "paid"},
{"id": 4, "amount": 300.0, "status": "unpaid"},
{"id": 5, "amount": 250.0, "status": "paid"}
]


c. Create a main.py (FastAPI App)
import importlib
from fastapi import FastAPI


create_invoice = importlib.import_module("01_create_invoice").router
get_invoices = importlib.import_module("01_get_invoices").router


app = FastAPI()
app.include_router(create_invoice)
app.include_router(get_invoices)


d.Update your get and create to use data store & model


from fastapi import APIRouter
from data_store import invoices
from models import Invoice


router = APIRouter()


@router.post("/invoices")


e.Start your main as uvicorn app and test it with postman