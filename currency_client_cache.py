import requests
import time

CACHE_EXPIRY=300 # 5 minutes

class CurrencyClientCache:
    def __init__(self, cache={}, cache_expiry=CACHE_EXPIRY):
        self.cache = cache
        self.cache_expiry = cache_expiry

    def request(self, url, headers):
        if url in self.cache and time.time() - self.cache[url]['timestamp'] < self.cache_expiry:
            response = self.cache[url]['response']
        else:
            response = requests.get(url, headers)
            self.cache[url] = {'response': response, 'timestamp': time.time()}
        return response
    
