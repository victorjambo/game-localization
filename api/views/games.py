from flask_restx import Resource
from main import rest_api
from flask import jsonify, request

from api.models import Game
from api.schemas.games import GameSchema

from main import db

@rest_api.route('/games')
class GamesResource(Resource):
    def get(self):
        """Fetch All Games"""

        games = Game.query.all()

        game_schema = GameSchema(many=True)

        data = game_schema.dump(games)

        return jsonify(games=data)

    def post(self):
        """Create New Game"""
        request_data = request.get_json()
        game_schema = GameSchema()
        game_data = game_schema.load(request_data)
        game = Game(**game_data)

        db.session.add(game)
        db.session.commit()

        return game_schema.dump(game), 201


@rest_api.route('/games/<string:game_id>')
class SingleGameResource(Resource):
    def get(self, game_id):
        """Fetch Single Game"""

        game = Game.query.filter_by(id=game_id).first()

        game_schema = GameSchema()

        return game_schema.dump(game)

    def put(self, game_id):
        """Update Game"""
        request_data = request.get_json()
        game_schema = GameSchema()
        game_data = game_schema.load(request_data)
        game = Game.query.filter_by(id=game_id).first()
        
        for field, value in game_data.items():
            setattr(game, field, value)

        db.session.add(game)
        db.session.commit()
        
        return game_schema.dump(game)

    def delete(self, game_id):
        """Soft Delete Game"""
        game = Game.query.filter_by(id=game_id).first()
        
        setattr(game, 'deleted', True)

        db.session.add(game)
        db.session.commit()

        return None, 204
