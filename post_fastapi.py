from fastapi import FastAPI
from models import Employee

app = FastAPI()


employees = []

@app.post("/employees")
def create_employee(employee: Employee):
    employees.append(employee.model_dump())

    return {
        "message": "Employee created successfully",
        "employee": employee
    }