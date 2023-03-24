import configparser, requests

config = configparser.ConfigParser()
config.read('config.ini')
headers = {'apikey': config['API']['key']}
url = config['API']['base_url']

def test_api_is_responding():
    response = requests.get(f'{url}?to=ARS&from=USD&amount=10000', headers=headers)
    assert response.status_code == 200

def test_api_returns_expected_data():
    response = requests.get(f'{url}?to=ARS&from=USD&amount=10000', headers=headers)
    data = response.json()
    assert 'date' in data
    assert 'info' in data
    assert 'rate' in data['info']
    assert 'timestamp' in data['info']
    assert 'query' in data
    assert 'amount' in data['query']
    assert 'from' in data['query']
    assert 'to' in data['query']
    assert 'result' in data
    assert 'success' in data
