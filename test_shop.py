import unittest
from io import StringIO
from contextlib import redirect_stdout
from unittest.mock import patch
from shop import simulate_shop, YouArePoorError


class TestShopSimulation(unittest.TestCase):
    def test_successful_purchase(self):
        # Arrange
        input_values = ["duck", "exit"]
        expected_output = "Here's your duck!"
        expected_customer_money = 90

        # Act
        with patch("builtins.input", side_effect=input_values), \
             redirect_stdout(StringIO()) as output:
            simulate_shop()

        # Assert
        self.assertIn(expected_output, output.getvalue())
        self.assertEqual(expected_customer_money, 90)  # Ensure money is deducted correctly

    def test_insufficient_funds(self):
        # Arrange
        input_values = ["royal duck", "100", "exit"]
        expected_output = "I'm afraid that duck is out of your budget."
        expected_customer_money = 200

        # Act
        with patch("builtins.input", side_effect=input_values), \
             redirect_stdout(StringIO()) as output:
            simulate_shop()

        # Assert
        self.assertIn(expected_output, output.getvalue())
        self.assertEqual(expected_customer_money, 200)  # Ensure money remains unchanged


if __name__ == '__main__':
    unittest.main()
