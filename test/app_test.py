import unittest
from chalice import BadRequestError
from app import app, password_compute_strength

password = '123a'

class MockRequest:
    def __init__(self, body):
        self.json_body = body

class TestRestEndpoint(unittest.TestCase):

    def test_normal_request(self):
        app.current_request = MockRequest(body = {
            'password': password
        })
        self.assertEqual(password_compute_strength(), {'strength': 4})

    def test_request_missing_password(self):
        app.current_request = MockRequest(body = {})
        try:
            password_compute_strength()
            self.fail('Should return BAD_REQUEST')
        except BadRequestError as err:
            self.assertEqual(str(err), 'BadRequestError: Password not provided')

if __name__ == '__main__':
    unittest.main()