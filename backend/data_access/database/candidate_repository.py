from data_access.database.session import get_session
from model.candidate import Candidate


class CandidateRepository:
    def select_all_candidates(self):
        session = get_session()
        return session.query(Candidate).order_by(Candidate.id).all()

    def create_candidate(self, candidate: Candidate):
        session = get_session()
        session.add(candidate)
        session.commit()

    def delete_candidate(self, candidate_id):
        session = get_session()
        session.query(Candidate).filter(Candidate.id == candidate_id).delete()
        session.commit()

    def update_candidate(self, new_candidate):
        session = get_session()
        if new_candidate.id is None:
            raise Exception("Id of candidate to be updated is not specified")
        candidate_to_update = session.query(Candidate).filter(Candidate.id == new_candidate.id).first()
        if new_candidate.name is not None:
            candidate_to_update.name = new_candidate.name
        if new_candidate.surname is not None:
            candidate_to_update.surname = new_candidate.surname
        if new_candidate.email is not None:
            candidate_to_update.email = new_candidate.email
        if new_candidate.experience is not None:
            candidate_to_update.experience = new_candidate.experience
        if new_candidate.technical_skills is not None:
            candidate_to_update.technical_skills = new_candidate.technical_skills
        if new_candidate.vacancy_id is not None:
            candidate_to_update.vacancy_id = new_candidate.vacancy_id
        session.commit()


if __name__ == '__main__':
    for candidate in CandidateRepository().select_all_candidates():
        print(candidate)
