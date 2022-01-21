from flask_restx import Resource
from main import rest_api
from flask import jsonify, request

from api.models import Game
from api.schemas.games import GameSchema, UpdateGameSchema
from api.utils.validators import validate_id


@rest_api.route('/games')
class GamesResource(Resource):
    def get(self):
        """Fetch All Games"""

        games = Game.query_(request.args)

        game_schema = GameSchema(many=True)

        data = game_schema.dump(games)

        return jsonify(games=data)

    def post(self):
        """Create New Game"""
        request_data = request.get_json()

        game_schema = GameSchema()
        game_data = game_schema.load(request_data)

        Game.get_by_name(game_data['name'])

        game = Game(**game_data)
        game.save()

        return game_schema.dump(game), 201


@rest_api.route('/games/<string:game_id>')
class SingleGameResource(Resource):
    @validate_id
    def get(self, game_id):
        """Fetch Single Game"""

        game = Game.get_or_404(game_id)

        game_schema = GameSchema()

        return game_schema.dump(game)

    @validate_id
    def put(self, game_id):
        """Update Game"""
        game = Game.get_or_404(game_id)

        request_data = request.get_json()
        game_schema = UpdateGameSchema()
        game_data = game_schema.load(request_data)

        game.update_(**game_data)

        return game_schema.dump(game)

    @validate_id
    def delete(self, game_id):
        """Soft Delete Game"""
        game = Game.get_or_404(game_id)

        game.update_(**{
            "deleted": True
        })

        return None, 204
