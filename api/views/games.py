from flask_restx import Resource
from main import rest_api
from flask import jsonify


@rest_api.route('/games')
class GamesResource(Resource):
    def get(self):
        """Fetch All Games"""
        return jsonify(dict(games=[
            {
                "id": "379d6e11-7024-1893-a209-84562b07b333",  # UUID4
                "name": "Final Fantasy",  # unique, not empty string
                # non-empty array of str
                "available_languages": ["en", "es", "de", "it", "fr", "ko"],
                "word_count": 82741003,  # positive int
                "release_date": "2022-01-11T12:36:38+00:00",  # null or ISO 8601 - always UTC
                "created_at": "2021-01-11T12:36:38+00:02"  # ISO 8601 - keeps client timezone
            }
        ]))

    def post(self):
        """Create New Game"""
        return {
            "id": "312e8e30-7624-4923-a805-84562b07b738",
            "name": "Diablo 112",
            "available_languages": ["en", "de", "ru", "it", "ko", "pt"],
            "word_count": 71701829,
            "release_date": "2022-01-11T12:36:38+00:00",
            "created_at": "2021-01-11T12:36:38+00:02"
        }


@rest_api.route('/games/<string:game_id>')
class SingleGameResource(Resource):
    def get(self, game_id):
        """Fetch Single Game"""
        return {
            "id": game_id,
            "name": "Diablo 112",
            "available_languages": ["en", "de", "ru", "it", "ko", "pt"],
            "word_count": 71701829,
            "release_date": "2022-01-11T12:36:38+00:00",
            "created_at": "2021-01-11T12:36:38+00:02"
        }

    def put(self, game_id):
        """Update Game"""
        return {
            "id": game_id,
            "name": "Super Mario World",
            "available_languages": ["en", "es", "de", "it", "fr", "ko"],
            "word_count": 91701298,
            "release_date": "2022-01-11T12:36:38+00:00",
            "created_at": "2021-01-11T12:36:38+00:02"
        }

    def delete(self, game_id):
        """Delete Game"""
        return jsonify(dict(success="OK"))
