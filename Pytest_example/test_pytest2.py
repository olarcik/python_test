import requests
import pytest
import allure

@allure.feature('Posts')
@allure.story('Get posts')
@pytest.mark.regression
def test_delete(new_post_id):
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}')
