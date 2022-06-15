from data_access.database.candidate_repository import CandidateRepository
from model.candidate import Candidate


class CandidateService:
    def __init__(self, candidate_repository: CandidateRepository):
        self.candidate_repository = candidate_repository

    def select_all_candidates(self):
        return self.candidate_repository.select_all_candidates()

    def create_candidate(self, candidate: Candidate):
        self.candidate_repository.create_candidate(candidate)

    def delete_candidate(self, vacancy_id):
        self.candidate_repository.delete_candidate(vacancy_id)

    def update_candidate(self, new_candidate):
        self.candidate_repository.update_candidate(new_candidate)