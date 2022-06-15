import json

from flask import Response, request

from flask.views import MethodView

from serializers.vacancy_serializer import VacancySchema
from service.vacancy_service import VacancyService


class VacancyController(MethodView):

    def __init__(self, vacancy_service: VacancyService):
        self.vacancy_service = vacancy_service

    def get(self):
        schema = VacancySchema()
        vacancies = self.vacancy_service.select_all_vacancies()
        vacancy_dicts = [schema.dump(vacancy) for vacancy in vacancies]
        response = Response(json.dumps(vacancy_dicts), status=200)
        return response

    def post(self):
        vacancy_request_record = request.get_json()
        print(vacancy_request_record)
        schema = VacancySchema()
        new_vacancy = schema.load(vacancy_request_record)
        self.vacancy_service.create_vacancy(new_vacancy)
        return Response(status=204)

    def delete(self, vacancy_id):
        self.vacancy_service.delete_vacancy(vacancy_id)
        return Response(status=200)

    def put(self):
        vacancy_request_record = request.get_json()
        print(vacancy_request_record)
        schema = VacancySchema()
        new_vacancy = schema.load(vacancy_request_record)
        self.vacancy_service.update_vacancy(new_vacancy)
        return Response(status=204)
