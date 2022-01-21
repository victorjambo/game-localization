import re

from main import db
from api.utils.validators import ValidationError


class ModelOperations(object):
    def save(self):
        """Save a model instance
        """
        db.session.add(self)
        db.session.commit()
        return self

    def update_(self, **kwargs):
        """update entries
        """
        for field, value in kwargs.items():
            setattr(self, field, value)
        db.session.commit()

    def delete(self):
        """Delete a model instance
        """
        db.session.delete(self)
        db.session.commit()
        return self

    @classmethod
    def query_(cls, order_conditions=None):
        """Dynamic filter
        """
        order = "release_date"

        if order_conditions \
            and order_conditions['sort_by'] \
            and order_conditions['sort_by'] in ['created_at', 'release_date']:
            order = order_conditions['sort_by']

        return cls.query.filter_by(deleted=False).order_by(order)

    @classmethod
    def get(cls, id):
        """Return entries by id
        """
        return cls.query.filter_by(id=id, deleted=False).first()

    @classmethod
    def get_or_404(cls, id):
        """Return entries by id
        """

        record = cls.get(id)

        if not record:
            raise ValidationError(
                {
                    'message':
                    f'{re.sub(r"(?<=[a-z])[A-Z]+",lambda x: f" {x.group(0).lower()}" , cls.__name__)} not found'
                },
                404)

        return record
    
    @classmethod
    def get_by_name(cls, name):
        """Return entries by name
        """
        record = cls.query.filter_by(name=name, deleted=False).first()

        if record:
            raise ValidationError(
                {
                    'message':
                    f'{re.sub(r"(?<=[a-z])[A-Z]+",lambda x: f" {x.group(0).lower()}" , cls.__name__)} with that name exists'
                },
                400)
