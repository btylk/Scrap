import unittest
import fivedots
from unittest.mock import patch, MagicMock

class processingTest(unittest.TestCase):
    @patch('fivedots.requests.get')
    def test_get_data(self, gmock):
        expected = '555'
        rmock = gmock()
        rmock.status_code = 200
        rmock.text = expected
        text = fivedots.get_fivedots_data()
        self.assertIn(expected, text)