from fastapi import APIRouter
from typing import List
from classroomactivityweek1day2.empmodels import employee
from classroomactivityweek1day2.data_store_emp import employees



router = APIRouter()

@router.post("/employees")
def create_employee(emp: employee):
    new_employee = emp.model_dump()
    employees.append(new_employee)
    return {"message": "Employee created successfully", "employee": new_employee}
