from marshmallow import Schema, fields, post_load

from model.hiring_progress import HiringProgress


class HiringProgressSchema(Schema):
    id = fields.Integer()
    hiring_stage = fields.Str()
    recruiter_feedback = fields.Str()
    technical_interviewer_feedback = fields.Str()
    technical_test_result = fields.Str()
    english_assessment_result = fields.Str()
    manager_feedback = fields.Str()
    candidate_id = fields.Integer()

    @post_load
    def make_hiring_progress(self, data, **kwargs):
        return HiringProgress(**data)
