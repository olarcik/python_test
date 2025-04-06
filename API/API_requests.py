from typing import assert_type

import requests


def all_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 99, 'Not all posts returned'

def one_post():
    post_id = 42
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}').json()
    assert response['id'] == post_id , 'Post ID is different than indicated'

def post_a_post():
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



def add_new_post():
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
    ).json()
    post_id = response['id']

    print(post_id)
    return post_id

def clear(post_id):
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')



def put_a_post():
    post_id = add_new_post()
    body = {
        "title": "foor",
        "body": "bars",
        "userId": 134,
    }
    headers = {
        'Content-Type' : 'application/json'
    }
    response = requests.put(
        f'https://jsonplaceholder.typicode.com/posts/{post_id}',
        json=body,
        headers=headers
    )
    assert response.json()['title'] == 'foor', 'Title was not chenged'
    clear(post_id)


put_a_post()





