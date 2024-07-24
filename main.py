from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
from models import DepartmentTbl, EmployeeTbl
from schema import DepartmentResponse, DepartmentCreate, EmployeeResponse, EmployeeCreate
from utils import send_mail, post_linkdin_imges
import uvicorn

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/create_department", response_model=DepartmentResponse)
async def create_department(department: DepartmentCreate, db: Session = Depends(get_db)):
    new_department = DepartmentTbl(name=department.name)
    db.add(new_department)
    db.commit()
    db.refresh(new_department)
    return new_department

@app.get("/get_department", response_model=list[DepartmentResponse])
async def get_departments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    departments = db.query(DepartmentTbl).offset(skip).limit(limit).all()
    return departments

@app.get("/get_department/{department_id}", response_model=DepartmentResponse)
async def get_departments(department_id: int, db: Session = Depends(get_db)):
    department = db.query(DepartmentTbl).filter(DepartmentTbl.id == department_id).first()
    if department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return department

@app.post("/employees/", response_model=EmployeeResponse)
async def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = EmployeeTbl(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    # Send welcome email
    await send_mail(to_email=[db_employee.email], user_obj=db_employee, mail_subject="", content="")

    # Notify department manager (placeholder)
    manager = db.query(EmployeeTbl).filter(EmployeeTbl.department_id == employee.department_id, EmployeeTbl.is_manager == True).first()
    if manager is not None:
        await send_mail(to_email=[manager.email], user_obj=db_employee, mail_subject="", content="")

    # Announce on social media (placeholder, using a dummy URL)
    text_content = f"Welcome {db_employee.first_name} {db_employee.last_name} to our department!"
    await post_linkdin_imges(title="post", text_content=text_content)

    return db_employee

@app.get("/get_employees/", response_model=list[EmployeeResponse])
async def get_employees(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    employees = db.query(EmployeeTbl).offset(skip).limit(limit).all()
    return employees

@app.get("/get_employees/{employee_id}", response_model=EmployeeResponse)
async def read_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(EmployeeTbl).filter(EmployeeTbl.id == employee_id).first()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@app.delete("/delete_employees/{employee_id}", response_model=EmployeeResponse)
async def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(EmployeeTbl).filter(EmployeeTbl.id == employee_id).first()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(employee)
    db.commit()
    return employee

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)