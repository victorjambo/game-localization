from .validators import ValidationError


def validate_duplicate(model, *query):
    """Validate duplicate fields from models
    """
    field, value = query
    entry = model.query.filter_by(deleted=False).filter(field == value).first()

    if entry is not None:
        raise ValidationError({'message': "{} exists".format(value)}, 400)
