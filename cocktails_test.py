import unittest
from unittest.mock import patch

from cocktails import get_ingredients, Cocktails

class Testing(unittest.TestCase):
    single_request = "Gin"
    malformed_multi_request = "Gin, Vodka"
    multi_request = "Gin,Vodka"

    def test_single_ingredient_length(self):
        """
        Test that when a known ingredient is used, length of list returned
        equals website example
        """
        ingredient = "Gin"
        cocktails = Cocktails(ingredient)
        self.assertEqual(len(cocktails.options), 100)

    def test_single_ingredient_first(self):
        """
        Test that when a known ingredient is used, first record is the same as
        website and direct Api call
        (could fail if any form of sorting was present on values)
        """
        ingredient = "Gin"
        cocktails = Cocktails(ingredient)
        self.assertEqual(cocktails.options[0], "3-Mile Long Island Iced Tea")

    def test_multi_ingredient(self):
        """
        Test that when multiple ingredients are specified,
        results aren't just returned from the initial ingredient
        """
        cocktails = Cocktails(self.multi_request)
        self.assertIn("Vodka And Tonic", cocktails.options)

    @patch('builtins.input', return_value=malformed_multi_request)
    def test_input_remove_spaces(self, mock_input):
        """
        uses dont always read instructions properly, can lead to invalid input
        in this case, spaces between words
        """

        expected = "Gin,Vodka"
        self.assertEqual(get_ingredients(), expected)


if __name__ == '__main__':
    unittest.main()
