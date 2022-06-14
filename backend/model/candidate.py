from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, Column, String, Float

Base = declarative_base()


class Candidate(Base):
    __tablename__ = 'candidate'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    experience = Column(Float)
    technical_skills = Column(String)
    vacancy_id = Column(Integer)

    def __repr__(self):
        return f"<Candidate(name={self.name}, surname={self.surname}, email={self.email}, " \
               f"experience={self.experience}, technical_skills={self.technical_skills}, vacancy_id={self.vacancy_id})>"
