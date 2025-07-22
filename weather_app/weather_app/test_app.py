import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Поиск погоды', response.data)

    def test_history_page(self):
        response = self.app.get('/history')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
