from flask import json

from main import api_prefix
from tests.mock import games_data, single_game


class TestGameResource:

    def test_get_all_games_with_no_games_succeeds(self, client, init_db):
        response = client.get(f"{api_prefix}/games")
        response_json = json.loads(response.data.decode("utf-8"))

        assert response.status_code == 200
        assert isinstance(response_json["games"], list)
        assert response_json["games"] == []

    def test_get_all_games_succeeds(self, client, init_db, new_game):
        new_game.save()

        response = client.get(f"{api_prefix}/games")
        response_json = json.loads(response.data.decode("utf-8"))

        assert response.status_code == 200
        assert isinstance(response_json["games"], list)
        assert response_json["games"][0]["name"] == new_game.name

    def test_get_single_game_succeeds(self, client, init_db, new_game):
        new_game.save()

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
        new_game.save()

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
        new_game.save()

        response = client.delete(f'{api_prefix}/games/{new_game.id}')

        assert response.status_code == 204

    def test_create_game_with_invalid_name_fails(self, client, init_db):
        data = single_game.copy()
        data["name"] = ""

        response = client.post(f'{api_prefix}/games', json=data)
        response_json = json.loads(response.data.decode("utf-8"))

        assert response.status_code == 400
        assert response_json["status"] == "error"
        assert response_json["message"] == "{'name': ['Shorter than minimum length 2.']}"

    def test_create_game_with_no_available_languages_fails(self, client, init_db):
        data = single_game.copy()
        data["available_languages"] = []

        response = client.post(f'{api_prefix}/games', json=data)
        response_json = json.loads(response.data.decode("utf-8"))

        assert response.status_code == 400
        assert response_json["status"] == "error"
        assert response_json["message"] == "{'available_languages': ['Shorter than minimum length 1.']}"

    def test_create_game_with_long_available_languages_string_fails(self, client, init_db):
        data = single_game.copy()
        data["available_languages"] = ["very long"]

        response = client.post(f'{api_prefix}/games', json=data)
        response_json = json.loads(response.data.decode("utf-8"))

        assert response.status_code == 400
        assert response_json["status"] == "error"
        assert response_json["message"] == """{'available_languages': {0: ['Longer than maximum length 2.']}}"""

    def test_create_game_with_invalid_word_count_fails(self, client, init_db):
        data = single_game.copy()
        data["word_count"] = "long"

        response = client.post(f'{api_prefix}/games', json=data)
        response_json = json.loads(response.data.decode("utf-8"))

        assert response.status_code == 400
        assert response_json["status"] == "error"
        assert response_json["message"] == "{'word_count': ['Not a valid integer.']}"

    def test_create_game_with_invalid_release_date_fails(self, client, init_db):
        data = single_game.copy()
        data["release_date"] = ""

        response = client.post(f'{api_prefix}/games', json=data)
        response_json = json.loads(response.data.decode("utf-8"))

        assert response.status_code == 400
        assert response_json["status"] == "error"
        assert response_json["message"] == "{'release_date': ['Not a valid datetime.']}"

    def test_create_game_duplicate_name_fails(self, client, init_db, new_game):
        new_game.save()
        data = single_game.copy()
        data["name"] = new_game.name

        response = client.post(f'{api_prefix}/games', json=data)
        response_json = json.loads(response.data.decode("utf-8"))

        assert response.status_code == 400
        assert response_json["message"] == "Game with that name exists"

    def test_create_game_with_deleted_name_succeeds(self, client, init_db, new_game_2):
        new_game_2.save()

        response = client.delete(f'{api_prefix}/games/{new_game_2.id}')

        assert response.status_code == 204

        data = single_game.copy()
        data["name"] = new_game_2.name

        response = client.post(f'{api_prefix}/games', json=data)
        response_json = json.loads(response.data.decode("utf-8"))

        assert response.status_code == 201
        assert response_json["name"] == data["name"]
