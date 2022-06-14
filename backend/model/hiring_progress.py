from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, Column, String

Base = declarative_base()


class HiringProgress(Base):
    __tablename__ = 'hiring_progress'
    id = Column(Integer, primary_key=True)
    hiring_stage = Column(String)
    recruiter_feedback = Column(String, nullable=True)
    technical_interviewer_feedback = Column(String, nullable=True)
    technical_test_result = Column(String, nullable=True)
    english_assessment_result = Column(String, nullable=True)
    manager_feedback = Column(String, nullable=True)
    candidate_id = Column(Integer)

    def __repr__(self):
        return f"<HiringProgress(hiring_stage={self.hiring_stage}, recruiter_feedback={self.recruiter_feedback}, " \
               f"technical_interviewer_feedback={self.technical_interviewer_feedback}, " \
               f"technical_test_result={self.technical_test_result}, " \
               f"english_assessment_result={self.english_assessment_result}, " \
               f"manager_feedback={self.manager_feedback}, candidate_id={self.candidate_id})>"
