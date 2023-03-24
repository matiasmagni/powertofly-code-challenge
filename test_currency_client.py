import unittest
from currency_client_cache import CurrencyClientCache
from currency_client import CurrencyClient

class TestCurrencyClient(unittest.TestCase):
    def setUp(self):
        cache = CurrencyClientCache()
        self.client = CurrencyClient(cache)

    def test_result_not_empty(self):
        self.assertGreater(self.client.get_currency_exchange('USD', 'EUR', 70000), 0)

    def test_same_currencies(self):
        self.assertEqual(self.client.get_currency_exchange('USD', 'USD', 5000), 5000)

    def test_zero_value_exception(self):
        with self.assertRaises(Exception) as context:
            self.client.get_currency_exchange('USD', 'EUR', 0)

    def test_negative_value_exception(self):
        with self.assertRaises(Exception) as context:
            self.client.get_currency_exchange('USD', 'EUR', -1)

if __name__ == '__main__':
    unittest.main()
