import unittest
from market_data import load_market_data


class TestMarketData(unittest.TestCase):
    def test_data_loading(self):
        prices, mu, sigma = load_market_data("AAPL", "1y")
        self.assertTrue(len(prices) > 0)
        self.assertTrue(sigma > 0)

if __name__ == "__main__":
    unittest.main()
