from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, Column, String, Boolean, Float

Base = declarative_base()


class Vacancy(Base):
    __tablename__ = 'vacancy'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    salary = Column(String)
    experience = Column(Float)
    is_urgent = Column(Boolean)
    seniority = Column(String)
    direction = Column(String)

    def __repr__(self):
        return f"<Vacancy(name={self.name}, description={self.description}, salary={self.salary}, " \
               f"experience={self.experience}, is_urgent={self.is_urgent}, seniority={self.seniority}, " \
               f"direction={self.direction})>"
