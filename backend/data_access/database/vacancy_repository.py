from data_access.database.session import get_session
from model.vacancy import Vacancy


def select_all_vacancies():
    session = get_session()
    return session.query(Vacancy).order_by(Vacancy.id).all()


def create_vacancy(vacancy: Vacancy):
    session = get_session()
    session.add(vacancy)
    session.commit()


def delete_vacancy(vacancy_id):
    session = get_session()
    session.query(Vacancy).filter(Vacancy.id == vacancy_id).delete()
    session.commit()


def update_vacancy(new_vacancy):
    session = get_session()
    if new_vacancy.id is None:
        raise Exception("Id of vacancy to be updated is not specified")
    vacancy_to_update = session.query(Vacancy).filter(Vacancy.id == new_vacancy.id).first()
    if new_vacancy.name is not None:
        vacancy_to_update.name = new_vacancy.name
    if new_vacancy.description is not None:
        vacancy_to_update.description = new_vacancy.description
    if new_vacancy.salary is not None:
        vacancy_to_update.salary = new_vacancy.salary
    if new_vacancy.experience is not None:
        vacancy_to_update.experience = new_vacancy.experience
    if new_vacancy.is_urgent is not None:
        vacancy_to_update.is_urgent = new_vacancy.is_urgent
    if new_vacancy.seniority is not None:
        vacancy_to_update.seniority = new_vacancy.seniority
    if new_vacancy.direction is not None:
        vacancy_to_update.direction = new_vacancy.direction
    session.commit()


if __name__ == '__main__':
    for vacancy in select_all_vacancies():
        print(vacancy)
