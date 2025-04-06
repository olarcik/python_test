import unittest
import requests
import sys

class TestPostApi(unittest.TestCase):

    @unittest.skip('No make sens now')
    def test_get_all_posts(self):
        response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
        self.assertEqual(len(response), 100)

    @unittest.skipIf(sys.platform == 'win32', 'Test not for linux')
    def test_add_post(self):
        def post_a_post():
            body = {
                "title": "foor",
                "body": "bars",
                "userId": 134,
            }
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.post(
                'https://jsonplaceholder.typicode.com/posts',
                json=body,
                headers=headers
            )
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json()['id'], 101)