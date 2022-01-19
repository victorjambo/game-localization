"""Model Schemas"""
from marshmallow import Schema, fields


class GameSchema(Schema):
    class Meta:
        exclude = ["deleted"]

    id = fields.String(dump_only=True)
    deleted = fields.Boolean(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    name = fields.String(required=True)
    word_count = fields.Integer(required=True)
    release_date = fields.DateTime(required=True)
    available_languages = fields.List(fields.String(), required=True)
