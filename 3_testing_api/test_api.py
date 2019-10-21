import pytest


def test_image_random(request_dogs):
    response = request_dogs.get(path="/breeds/image/random")
    assert response.status_code == 200


def test_list_all(request_dogs):
    response = request_dogs.get(path="/breeds/list/all")
    assert response.json != []


def test_akita_in_all(request_dogs):
    response = request_dogs.get(path="/breeds/list/all")
    assert "akita" in response.json()["message"]


@pytest.mark.parametrize('breed', ['affenpinscher', 'african', 'airedale'])
def test_random_parametrize(request_dogs, breed):
    response = request_dogs.get(path='/breed/' + breed + '/images/random')
    assert response.status_code == 200


@pytest.mark.parametrize('breed', ['affenpinscher', 'african', 'airedale'])
def test_random_parametrize2(request_dogs, breed):
    response = request_dogs.get(path="/breeds/list/all")
    assert breed in response.json()["message"]


def test_list_breweries(request_breweries):
    response = request_breweries.get()
    assert response.status_code == 200


def test_autocomplete(request_breweries):
    response = request_breweries.get(path="/autocomplete?query=dog")
    assert response.json != []


def test_search(request_breweries):
    response = request_breweries.get(path="/search?query=dog")
    assert response.json != []


@pytest.mark.parametrize('state', ['Alabama', 'Alaska', 'Arizona'])
def test_sort_by_state(request_breweries, state):
    response = request_breweries.get(path='?by_state=' + state)
    assert response.status_code == 200


@pytest.mark.parametrize('id', ['44', '46', '55'])
def test_sort_by_id(request_breweries, id):
    response = request_breweries.get(path='/' + id)
    assert response.status_code == 200


def test_get_all(request_jsonplaceholder):
    response = request_jsonplaceholder.get(path='post')
    assert response.status_code == 200


def test_get_for_id(request_jsonplaceholder):
    response = request_jsonplaceholder.get(path='post/22')
    assert response.status_code == 200


def test_post_request(request_jsonplaceholder):
    response = request_jsonplaceholder.post(
        path='posts',
        data={'title': 'favilla',
              'body': 'favilla et cinere',
              'userId': 1
              })
    assert response.status_code == 201


@pytest.mark.parametrize('post_id', ['1', '2', '3'])
def test_comment_for_id(request_jsonplaceholder, post_id):
    response = request_jsonplaceholder.get(path='comments?postId=' + post_id)
    assert response.status_code == 200


@pytest.mark.parametrize('user_id', ['1', '2', '3'])
def test_comment_for_id(request_jsonplaceholder, user_id):
    response = request_jsonplaceholder.get(path='posts?userId=1' + user_id)
    assert response.status_code == 200
