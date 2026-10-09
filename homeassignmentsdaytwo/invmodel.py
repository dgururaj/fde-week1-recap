from pydantic import BaseModel

class invoice(BaseModel):
    invoice_id: str
    vendor: str
    amount: int
    status: str