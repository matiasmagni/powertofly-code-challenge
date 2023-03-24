import configparser
import logging


class CurrencyClient:

    def __init__(self, cache):
        logging.basicConfig(
            filename='app.log',
            encoding='utf-8',
            level=logging.DEBUG,
            format='%(asctime)s - %(message)s',
            datefmt='%m/%d/%y - %H:%M:%S'
        )
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.headers = {'apikey': config['API']['key']}
        self.url = config['API']['base_url']
        self.cache = cache

    def get_currency_exchange(self, from_currency, to_currency, amount):
        result = None
        response = self.cache.request(
            f'{self.url}?to={to_currency}&from={from_currency}&amount={amount}', headers=self.headers
        )

        if not response.json().get('error'):
            result = response.json()['result']
            logging.info({ f'{amount} {from_currency}': f'{result} {to_currency}' })
        else:
            raise ValueError(response.json()['error']['message']);

        return result

    def set_interval(self, cache_expiry):
        self.cache.cache_expiry = cache_expiry
