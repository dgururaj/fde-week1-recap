from pydantic import BaseModel

class employee(BaseModel):
    id: int
    name: str
    position: str
    city: str
