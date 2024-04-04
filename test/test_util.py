import unittest
import numpy as np
from dummyfw.util import mean


class TestMeanFunction(unittest.TestCase):

    def test_mean_positive_numbers(self):
        """Testa a média de números positivos."""
        vec = np.array([1, 2, 3, 4, 5])
        self.assertAlmostEqual(mean(vec), 3.0, "A média de números positivos não foi calculada corretamente.")

    def test_mean_negative_numbers(self):
        """Testa a média de números negativos."""
        vec = np.array([-1, -2, -3, -4, -5])
        self.assertAlmostEqual(mean(vec), -3.0, "A média de números negativos não foi calculada corretamente.")

    def test_mean_mixed_numbers(self):
        """Testa a média de números mistos."""
        vec = np.array([-1, 2, -3, 4, 5])
        self.assertAlmostEqual(mean(vec), 1.4, "A média de números mistos não foi calculada corretamente.")


