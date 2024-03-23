import json
from flask_testing import TestCase
from app import app

class TestFlaskApi(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_predict(self):
        # Simulate a POST request
        response = self.client.post('/predict', data=json.dumps({'text': "I am happy"}),
                                    content_type='application/json')
        data = json.loads(response.data)

        # Check status code and response structure
        self.assertEqual(response.status_code, 200)
        self.assertIn('emotion', data)
