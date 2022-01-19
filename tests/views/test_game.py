from flask import json

from main import db, api_prefix
from tests.mock import games_data


class TestGameResource:

    def test_get_all_games_succeeds(self, client, init_db, new_game):
        db.session.add(new_game)
        db.session.commit()

        response = client.get(f"{api_prefix}/games")
        response_json = json.loads(response.data.decode("utf-8"))

        assert response.status_code == 200
        assert isinstance(response_json["games"], list)
        assert response_json["games"][0]["name"] == new_game.name

    def test_get_single_game_succeeds(self, client, init_db, new_game):
        db.session.add(new_game)
        db.session.commit()

        response = client.get(f"{api_prefix}/games/{new_game.id}")
        response_json = json.loads(response.data.decode("utf-8"))

        assert response.status_code == 200
        assert response_json["name"] == new_game.name

    def test_create_game_succeeds(self, client, init_db):
        data = games_data[-1]

        response = client.post(f'{api_prefix}/games', json=data)
        response_json = json.loads(response.data.decode("utf-8"))

        assert response.status_code == 201
        assert response_json["name"] == data["name"]

    def test_update_game_succeeds(self, client, init_db, new_game):
        db.session.add(new_game)
        db.session.commit()

        data = {
            "name": "RALLY",
            "available_languages": ["it"],
            "word_count": 5555,
            "release_date": "2022-01-11T12:36:38+00:00"
        }
        old_name = new_game.name

        response = client.put(f'{api_prefix}/games/{new_game.id}', json=data)
        response_json = json.loads(response.data.decode("utf-8"))

        assert response.status_code == 200
        assert response_json["id"] == str(new_game.id)
        assert response_json["name"] == data["name"]
        assert response_json["name"] != old_name

    def test_soft_delete_game_succeeds(self, client, init_db, new_game):
        db.session.add(new_game)
        db.session.commit()

        response = client.delete(f'{api_prefix}/games/{new_game.id}')

        assert response.status_code == 204
