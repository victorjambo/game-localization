"""Model Schemas"""
from marshmallow import Schema, fields, validate
from api.utils.validators import ValidationError


class GameSchema(Schema):
    class Meta:
        exclude = ["deleted"]

    id = fields.UUID(dump_only=True)
    deleted = fields.Boolean(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=2))
    word_count = fields.Int(required=True)
    release_date = fields.DateTime(required=True)
    available_languages = fields.List(fields.Str(validate=validate.Length(
        max=2)), required=True, validate=validate.Length(min=1))

    def handle_error(self, exc, data, **kwargs):
        """Log and raise our custom exception when (de)serialization fails."""
        raise ValidationError({
            "message": f"{exc}"
        }, 400)


class UpdateGameSchema(GameSchema):

    name = fields.String()
    word_count = fields.Integer()
    release_date = fields.DateTime()
    available_languages = fields.List(fields.String())
