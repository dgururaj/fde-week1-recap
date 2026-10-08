from fastapi import FastAPI
import importlib

create_employee = importlib.import_module("classroomactivityweek1day2.create_employee").router
get_employee = importlib.import_module("classroomactivityweek1day2.get_employee").router

app = FastAPI()
app.include_router(create_employee)
app.include_router(get_employee)