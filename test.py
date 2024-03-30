import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), "Welcome to the Iris Flower Prediction API!")

    def test_predict(self):
        data = {
            'sepal_length': 5.1,
            'sepal_width': 3.5,
            'petal_length': 1.4,
            'petal_width': 0.2
        }
        response = self.app.post('/predict', json=data)
        self.assertEqual(response.status_code, 200)
        prediction = response.json['prediction']
        self.assertIsInstance(prediction, int)

if __name__ == '__main__':
    unittest.main()
