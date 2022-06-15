from marshmallow import Schema, fields, post_load

from model.vacancy import Vacancy


class VacancySchema(Schema):
    id = fields.Integer()
    name = fields.Str()
    description = fields.Str()
    salary = fields.Str()
    experience = fields.Float()
    is_urgent = fields.Boolean()
    seniority = fields.Str()
    direction = fields.Str()

    @post_load
    def make_vacancy(self, data, **kwargs):
        return Vacancy(**data)
