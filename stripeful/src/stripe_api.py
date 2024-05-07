import requests
import logging

from constants import Constants

logging.basicConfig(level=logging.INFO)

class StripeFetcher:

    def __init__(self):
        self.api_url = 'https://api.stripe.com/v1/customers'
        logging.info('Stripe Fetcher Object Initialised')

    def create_customer_form_url_encoded(self):
        body = {
            'name': 'test_name',
            'description': 'test_description',
            'email': 'test_email@gmail.com',
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Bearer {0}'.format(Constants.STRIPE_API_KEY)
        }

        response = requests.post(self.api_url, data=body, headers=headers)
        logging.info('Stripe customer creation status: {0}'.format(response.status_code))
        return response

    # Note: Stripe does not handle json request bodys, and as a result will create a customer with empty information.
    #       Use the method above for that to function correctly.
    def create_customer_json(self):
        body = {
            'name': 'test_name',
            'description': 'test_description',
            'email': 'test_email@gmail.com',
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Bearer {0}'.format(Constants.STRIPE_API_KEY)
        }

        response = requests.post(self.api_url, json=body, headers=headers)
        logging.info('Stripe customer creation status: {0}'.format(response.status_code))
        return response


def main():
    fetcher = StripeFetcher()
    fetcher.create_customer_form_url_encoded()

if __name__ == "__main__":
    main()
