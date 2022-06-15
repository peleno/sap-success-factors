from marshmallow import Schema, fields, post_load

from model.candidate import Candidate


class CandidateSchema(Schema):
    id = fields.Integer()
    name = fields.Str()
    surname = fields.Str()
    email = fields.Str()
    experience = fields.Float()
    technical_skills = fields.Str()
    vacancy_id = fields.Integer()
    
    @post_load
    def make_candidate(self, data, **kwargs):
        return Candidate(**data)
