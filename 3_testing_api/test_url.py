def test_url(request_url):
    assert request_url.get().status_code == 200
