import uuid
from main import db
from sqlalchemy.dialects.postgresql import ARRAY, UUID


class Game(db.Model):
    """Game Model"""
    __tablename__ = 'games'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    available_languages = db.Column(ARRAY(db.String), nullable=False)
    word_count = db.Column(db.Integer, nullable=False)
    release_date = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Game {self.name}>'
