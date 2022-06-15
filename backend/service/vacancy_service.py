from data_access.csv.vacancy_csv_reader import VacancyCsvReader
from data_access.database.vacancy_repository import VacancyRepository
from model.vacancy import Vacancy


class VacancyService:
    def __init__(self, vacancy_repository: VacancyRepository, vacancy_csv_reader: VacancyCsvReader):
        self.vacancy_repository = vacancy_repository
        self.vacancy_csv_reader = vacancy_csv_reader

    def select_all_vacancies(self):
        return self.vacancy_repository.select_all_vacancies()

    def create_vacancy(self, vacancy: Vacancy):
        self.vacancy_repository.create_vacancy(vacancy)

    def delete_vacancy(self, vacancy_id):
        self.vacancy_repository.delete_vacancy(vacancy_id)

    def update_vacancy(self, new_vacancy):
        self.vacancy_repository.update_vacancy(new_vacancy)

    def load_database_from_csv(self):
        vacancies_from_csv = self.vacancy_csv_reader.read_vacancies_from_csv()

        for vacancy in vacancies_from_csv:
            self.create_vacancy(vacancy)


if __name__ == '__main__':
    VacancyService(VacancyRepository(), VacancyCsvReader()).load_database_from_csv()
