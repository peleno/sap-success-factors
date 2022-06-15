import csv

from model.vacancy import Vacancy

CSV_FILENAME = '/home/andrii/Study/NULP/Course3/documenting/sap-success-factors/backend/utils/vacancies.csv'


class VacancyCsvReader:

    def read_vacancies_from_csv(self):
        with open(CSV_FILENAME, 'r') as f:
            reader = csv.reader(f)
            vacancies = []
            for row in reader:
                vacancy = Vacancy(name=row[0],
                                  description=row[1],
                                  salary=row[2],
                                  experience=row[3],
                                  is_urgent=row[4] == 'True',
                                  seniority=row[5],
                                  direction=row[6])
                vacancies.append(vacancy)
            return vacancies


if __name__ == '__main__':
    print(VacancyCsvReader().read_vacancies_from_csv())
