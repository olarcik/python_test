import requests
import pytest
import allure

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
    print('Deleting post')
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')

@pytest.fixture(scope='session')
def hello():
    print('hello')
    yield
    print('bye')


@allure.feature('Get posts')
@allure.story('Posts')
@pytest.mark.regression
def test_get_one_post(new_post_id, hello):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}').json()
    assert response['id'] == new_post_id , 'Post ID is different than indicated'

@allure.feature('Get posts')
@allure.story('Posts')
@pytest.mark.regression
def test_get_all_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100

@allure.feature('Manipulate posts')
@allure.story('Posts')
@pytest.mark.regression
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

@allure.feature('Equals')
@allure.story('Example')
@pytest.mark.smoke
def test_one():
    assert 1 == 1

@allure.feature('Equals')
@allure.story('Example')
@pytest.mark.smoke
def test_two():
    assert 1 == 1

@allure.feature('Equals')
@allure.story('Example')
@pytest.mark.smoke
@pytest.mark.parametrize('logins', ['', ' ', '(*&^'])
def test_three(logins):
    print('')
    assert 1 == 1