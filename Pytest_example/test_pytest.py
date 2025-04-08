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


@allure.feature('Posts')
@allure.story('Get posts')
@pytest.mark.regression
def test_get_one_post(new_post_id, hello):
    with allure.step(f'Run get request for post with id {new_post_id}'):
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}').json()
    with allure.step(f'Check if the post is {new_post_id}'):
        assert response['id'] == new_post_id , 'Post ID is different than indicated'

@allure.feature('Posts')
@allure.story('Get posts')
@pytest.mark.regression
def test_get_all_posts():
    with allure.step('Run get request to see list of all posts'):
        response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    with allure.step('Validate the len of the list, in the list should be 100 items'):
        assert len(response) == 100

@allure.feature('Posts')
@allure.story('Manipulate posts')
@allure.title('Create a new post')
@allure.issue('https://en.wikipedia.org/wiki/TestLink')
@pytest.mark.regression
def test_post_a_post():
    with allure.step('Sent user data to register a new user'):
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

    with allure.step('Check the response status code'):
        assert response.status_code == 404, f'Status code is incorrect, status code is {response.status_code}'
    with allure.step('Check if created user`s id is correct'):
        assert response.json()['id'] == 101, 'Id is incorrect'

@allure.feature('Example')
@allure.story('Equals')
@pytest.mark.smoke
def test_one():
    with allure.step('Validate the result of function'):
        assert 1 == 1

@allure.feature('Example')
@allure.story('Equals')
@pytest.mark.smoke
def test_two():
    assert 1 == 1

@allure.feature('Example')
@allure.story('Equals')
@pytest.mark.smoke
@pytest.mark.parametrize('logins', ['', ' ', '(*&^'])
def test_three(logins):
    print('')
    assert 1 == 1