import unittest
import numpy as np
from metrics import *

class TestMetrics(unittest.TestCase):
    def test_expected_return(self):
        final_prices = np.array([110, 120, 130])
        result = expected_return(final_prices, 100)
        self.assertAlmostEqual(result, 20)

    def test_var(self):
        final_prices = np.array([80, 90, 100, 110, 120])
        result = var_95(final_prices, 100)
        self.assertTrue(result >= 0)

    def test_probability_loss(self):
        final_prices = np.array([80, 90, 110, 120])
        result = probability_loss(final_prices, 100)
        self.assertEqual(result, 50.0)

    def test_sharpe(self):
        final_prices = np.array([110, 120, 130])
        result = sharpe_ratio(final_prices, 100)
        self.assertTrue(result > 0)

    def test_max_drawdown(self):
        path = np.array([100, 120, 80, 90])
        result = max_drawdown(path)
        self.assertLess(result, 0)


if __name__ == "__main__":
    unittest.main()
