from data_access.database.hiring_progress_repository import HiringProgressRepository
from model.hiring_progress import HiringProgress


class HiringProgressService:
    def __init__(self, hiring_progress_repository: HiringProgressRepository):
        self.hiring_progress_repository = hiring_progress_repository

    def select_all_hiring_progresses(self):
        return self.hiring_progress_repository.select_all_hiring_progresses()

    def create_hiring_progress(self, hiring_progress: HiringProgress):
        self.hiring_progress_repository.create_hiring_progress(hiring_progress)

    def delete_hiring_progress(self, hiring_progress_id):
        self.hiring_progress_repository.delete_hiring_progress(hiring_progress_id)

    def update_hiring_progress(self, new_hiring_progress):
        self.hiring_progress_repository.update_hiring_progress(new_hiring_progress)
