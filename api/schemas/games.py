"""Model Schemas"""
from marshmallow import Schema, fields
from api.utils.validators import ValidationError


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

    def handle_error(self, exc, data, **kwargs):
        """Log and raise our custom exception when (de)serialization fails."""
        raise ValidationError({
            "message": "An error occurred with input: {0}".format(data)
        }, 400)

class UpdateGameSchema(GameSchema):

    name = fields.String()
    word_count = fields.Integer()
    release_date = fields.DateTime()
    available_languages = fields.List(fields.String())
