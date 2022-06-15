import csv
from random import randint

SENIORITY_LEVELS = {"Intern": [0, 1], "Junior": [0.5, 1.5], "Middle": [1.5, 4], "Senior": [4, 6], "Principal": [6, 15]}
DEV_TECHNOLOGIES = ["Java", "Python", "Embedded", "C#", "JavaScript", "Rust", "Full Stack"]
NON_DEV_DIRECTIONS = ["HR", "Management", "QA", "UI/UX", "Support", "DevOps", "Data Science"]
VACANCY_DIRECTIONS = DEV_TECHNOLOGIES + NON_DEV_DIRECTIONS

CSV_ROWS_COUNT = 1000
CSV_FILENAME = 'vacancies.csv'


def get_description_for_dev_position(technology):
    return f"We are looking for {technology} developer who will become a great part of our team."


def get_description_for_non_dev_positions(direction):
    return f"We are looking for {direction} specialist who will become a great part of our team."


def generate_random_vacancy_row():
    direction = VACANCY_DIRECTIONS[randint(0, len(VACANCY_DIRECTIONS) - 1)]
    seniority = list(SENIORITY_LEVELS.keys())[randint(0, len(SENIORITY_LEVELS) - 1)]
    if direction in DEV_TECHNOLOGIES:
        description = get_description_for_dev_position(direction)
        name = ' '.join([seniority, direction, 'Developer'])
    else:
        description = get_description_for_non_dev_positions(direction)
        name = ' '.join([seniority, direction, 'Specialist'])
    experience = SENIORITY_LEVELS[seniority][0] \
        + 0.5 * randint(0, int((SENIORITY_LEVELS[seniority][1] - SENIORITY_LEVELS[seniority][0]) / 0.5))

    salary = 1000 * int(experience) + 100 * randint(0, 3)
    is_urgent = bool(randint(0, 1))
    vacancy_row = [name, description, salary, experience, is_urgent, seniority, direction]
    return vacancy_row


def generate_csv_for_vacancies():
    with open(CSV_FILENAME, 'w') as f:
        writer = csv.writer(f)
        for i in range(CSV_ROWS_COUNT):
            vacancy_row = generate_random_vacancy_row()
            writer.writerow(vacancy_row)


if __name__ == '__main__':
    generate_csv_for_vacancies()
