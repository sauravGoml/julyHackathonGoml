from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class DepartmentTbl(Base):
    __tablename__ = 'department_tbl'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    employees = relationship("EmployeeTbl", back_populates="department")

class EmployeeTbl(Base):
    __tablename__ = 'employees_tbl'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    is_manager = Column(Boolean, nullable=True)
    department_id = Column(Integer, ForeignKey('department_tbl.id'))

    department = relationship("DepartmentTbl", back_populates="employees")