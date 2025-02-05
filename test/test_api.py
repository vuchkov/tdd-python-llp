import unittest
import json
from flask import request

from app import app

class TestApi(unittest.TestCase):

    def test_llp_endpoint_given_json_body_returns_200(self):
        with app.test_client() as client:
            response = client.post('/llp', json={"sentence": "Steve Malkmus is in a good band."})
            assert response._status_code == 200

    def test_llp_endpoint_given_json_body_returns_entity_result_in_response(self):
        with app.test_client() as client:
            response = client.post('/llp', json={"sentence": "Donald Trump"})
            data = json.loads(response.get_data())
            assert data["entities"] is not None and len(data["entities"]) > 0
            assert data["entities"][0]['ent'] == 'Donald Trump'
            assert data["entities"][0]['label'] == 'Person'