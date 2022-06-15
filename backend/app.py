from flask import Flask

from controllers.candidate_controller import CandidateController
from controllers.hiring_progress_controller import HiringProgressController
from controllers.vacancy_controller import VacancyController
from data_access.csv.vacancy_csv_reader import VacancyCsvReader
from data_access.database.candidate_repository import CandidateRepository
from data_access.database.hiring_progress_repository import HiringProgressRepository
from data_access.database.vacancy_repository import VacancyRepository
from service.candidate_service import CandidateService
from service.hiring_progress_service import HiringProgressService
from service.vacancy_service import VacancyService

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


app.add_url_rule('/vacancy/', view_func=VacancyController.as_view(
    'vacancies', VacancyService(VacancyRepository(), VacancyCsvReader())))
app.add_url_rule('/vacancy/<int:vacancy_id>', view_func=VacancyController.as_view(
    'vacancy', VacancyService(VacancyRepository(), VacancyCsvReader())))

app.add_url_rule('/candidate/', view_func=CandidateController.as_view(
    'candidates', CandidateService(CandidateRepository())))
app.add_url_rule('/candidate/<int:candidate_id>', view_func=CandidateController.as_view(
    'candidate', CandidateService(CandidateRepository())))

app.add_url_rule('/hiring_progress/', view_func=HiringProgressController.as_view(
    'hiring_progresses', HiringProgressService(HiringProgressRepository())))
app.add_url_rule('/hiring_progress/<int:hiring_progress_id>', view_func=HiringProgressController.as_view(
    'hiring_progress', HiringProgressService(HiringProgressRepository())))

if __name__ == '__main__':
    app.run()
