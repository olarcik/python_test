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
    return post_id




def test_get_one_post(new_post_id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}').json()
    assert response['id'] == new_post_id , 'Post ID is different than indicated'


def test_get_all_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100


def test_post_a_post():
    print('Vlad sexy')
    body = {
        "title": "foor",
        "body": "bars",
        "userId": 134,
    }
    headers = {
        'Content-Type' : 'application/json'
    }
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    )

    assert response.status_code == 201, f'Status code is incorrect, status code is {response.status_code}'
    assert response.json()['id'] == 101, 'Id is incorrect'