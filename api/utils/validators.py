"""Module for Validation error and error handler"""
from uuid import UUID
from functools import wraps


class ValidationError(Exception):
    """Base Validation class for handling validation errors"""

    def __init__(self, error, status_code=None):
        Exception.__init__(self)
        self.status_code = 400
        self.error = error
        self.error['status'] = 'error'
        self.error['message'] = error['message']

        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return self.error


def validate_id(func):
    """Decorator to validate id
    """

    @wraps(func)
    def decorated_function(*args, **kwargs):
        check_id_valid(**kwargs)
        return func(*args, **kwargs)

    return decorated_function


def check_id_valid(**kwargs):
    for key in kwargs:
        if key.endswith("_id") and not is_valid_uuid(kwargs.get(key, None)):
            raise ValidationError({
                "status": "error",
                "message": "invalid id"
            }, 400)


def is_valid_uuid(uuid_id):
    try:
        uuid_obj = UUID(uuid_id, version=4)
    except ValueError:
        return False
    return str(uuid_obj) == uuid_id
