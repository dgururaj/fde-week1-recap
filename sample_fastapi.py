# sample_fastapi.py implements a simple FastAPI server with endpoints to retrieve employee data.
from fastapi import FastAPI
from typing import List

app = FastAPI(
    title="Employee API",
    description="Simple FastAPI example",
    version="1.0.0"
)

employees = [
    {"id": 1, "name": "John Doe", "position": "Software Engineer"},
    {"id": 2, "name": "Jane Smith", "position": "Data Scientist"},
    {"id": 3, "name": "Mike Johnson", "position": "Product Manager"},
]


@app.get("/")
def home():
    return {"message": "FastAPI server is running"}


@app.get("/employees")
def get_employees():
    return employees


@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee

    return {"error": "Employee not found"}