import sys
import unittest

sys.path.append('../../stripeful/src/')

from stripe_api import StripeFetcher

class TestCustomerManagement(unittest.TestCase):

    def test_request_to_stripe_api_when_post_to_customer_creation_then_should_create_customer_successfully(self):
        stripe_fetcher = StripeFetcher()
        response = stripe_fetcher.create_customer_form_url_encoded()
        self.assertEqual(response.status_code, 200, "http status code should be 200")
        # Contains operation
        self.assertIn("test_email@gmail.com", response.text, "email key is expected to be in response body")

if __name__ == '__main__':
    unittest.main()
