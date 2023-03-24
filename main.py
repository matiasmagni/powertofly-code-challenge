from currency_client_cache import CurrencyClientCache
from currency_client import CurrencyClient

def main():
    cache = CurrencyClientCache()
    client = CurrencyClient(cache)
    client.get_currency_exchange('USD', 'ARS', 70000)
    client.get_currency_exchange('USD', 'ARS', 70000)
    client.set_interval(35)
    client.get_currency_exchange('USD', 'EUR', 70000)

if __name__ == "__main__":
    main()
