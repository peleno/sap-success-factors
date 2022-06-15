import json

from flask import Response, request
from flask.views import MethodView

from serializers.candidate_serializer import CandidateSchema
from service.candidate_service import CandidateService


class CandidateController(MethodView):

    def __init__(self, candidate_service: CandidateService):
        self.candidate_service = candidate_service

    def get(self):
        schema = CandidateSchema()
        candidates = self.candidate_service.select_all_candidates()
        candidate_dicts = [schema.dump(candidate) for candidate in candidates]
        response = Response(json.dumps(candidate_dicts), status=200)
        return response

    def post(self):
        candidate_request_record = request.get_json()
        print(candidate_request_record)
        schema = CandidateSchema()
        new_candidate = schema.load(candidate_request_record)
        self.candidate_service.create_candidate(new_candidate)
        return Response(status=204)

    def delete(self, candidate_id):
        self.candidate_service.delete_candidate(candidate_id)
        return Response(status=200)

    def put(self):
        candidate_request_record = request.get_json()
        print(candidate_request_record)
        schema = CandidateSchema()
        new_candidate = schema.load(candidate_request_record)
        self.candidate_service.update_candidate(new_candidate)
        return Response(status=204)
