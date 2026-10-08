from fastapi import APIRouter
from typing import List
from classroomactivityweek1day2.empmodels import employee
from classroomactivityweek1day2.data_store_emp import employees

router = APIRouter()

@router.get("/employees")
def get_employees():
    return employees


@router.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for emp in employees:
        if emp["id"] == employee_id:
            return emp

    return {"error": "Employee not found"}