

class TestBaseApi:
    def test_index(self, client):
        assert client.get('/').status_code == 200

    def test_index2(self, client):
        assert client.get('/').status_code == 200