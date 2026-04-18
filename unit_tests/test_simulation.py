import unittest
import numpy as np
from gbm import monte_carlo


class TestSimulation(unittest.TestCase):
    def test_output_shape(self):
        results = monte_carlo(100, 0.1, 0.2, 1, 1000)
        self.assertEqual(results.shape[1], 1000)

    def test_positive_values(self):
        results = monte_carlo(100, 0.1, 0.2, 1, 1000)
        self.assertTrue(np.all(results > 0))

    def test_reproducibility(self):
        np.random.seed(42)
        r1 = monte_carlo(100, 0.1, 0.2, 1, 10)
        np.random.seed(42)
        r2 = monte_carlo(100, 0.1, 0.2, 1, 10)
        self.assertTrue(np.allclose(r1, r2))

if __name__ == "__main__":
    unittest.main()
