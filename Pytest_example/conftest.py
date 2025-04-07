import requests
import pytest

@pytest.fixture()
def new_post_id():
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
    post_id = response.json()['id']
    print(f'Post created: {post_id}')
    yield post_id
