import requests

from constants import Constants

def main():
    create_customer_form_url_encoded()

def create_customer_form_url_encoded():
    url = 'https://api.stripe.com/v1/customers'
    body = {
        'name': 'test_name',
        'description': 'test_description',
        'email': 'test_email@gmail.com',
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer {0}'.format(Constants.STRIPE_API_KEY)
    }

    response = requests.post(url, data=body, headers=headers)
    print(response.status_code, response.text)

# Note: Stripe does not handle json request bodys, and as a result will create a customer with empty information.
#       Use the method above for that to function correctly.
def create_customer_json():
    url = 'https://api.stripe.com/v1/customers'
    body = {
        'name': 'test_name',
        'description': 'test_description',
        'email': 'test_email@gmail.com',
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer {0}'.format(Constants.STRIPE_API_KEY)
    }

    response = requests.post(url, json=body, headers=headers)
    print(response.status_code, response.text)

if __name__ == "__main__":
    main()
