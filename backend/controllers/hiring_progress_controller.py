import json

from flask import Response, request
from flask.views import MethodView

from serializers.hiring_progress_serializer import HiringProgressSchema
from service.hiring_progress_service import HiringProgressService


class HiringProgressController(MethodView):

    def __init__(self, hiring_progress_service: HiringProgressService):
        self.hiring_progress_service = hiring_progress_service

    def get(self):
        schema = HiringProgressSchema()
        hiring_progresses = self.hiring_progress_service.select_all_hiring_progresses()
        hiring_progress_dicts = [schema.dump(hiring_progress) for hiring_progress in hiring_progresses]
        response = Response(json.dumps(hiring_progress_dicts), status=200)
        return response

    def post(self):
        hiring_progress_request_record = request.get_json()
        print(hiring_progress_request_record)
        schema = HiringProgressSchema()
        new_hiring_progress = schema.load(hiring_progress_request_record)
        self.hiring_progress_service.create_hiring_progress(new_hiring_progress)
        return Response(status=204)

    def delete(self, hiring_progress_id):
        self.hiring_progress_service.delete_hiring_progress(hiring_progress_id)
        return Response(status=200)

    def put(self):
        hiring_progress_request_record = request.get_json()
        print(hiring_progress_request_record)
        schema = HiringProgressSchema()
        new_hiring_progress = schema.load(hiring_progress_request_record)
        self.hiring_progress_service.update_hiring_progress(new_hiring_progress)
        return Response(status=204)
