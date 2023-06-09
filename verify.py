import random
import string
import requests
from pprint import pprint
from paystackapi.paystack import Paystack
from paystackapi.plan import Plan
from paystackapi.transaction import Transaction

EMAIL = "famos204@gmail.com"

SECRET_KEY = "sk_test_4f188e63dc16982fc116eb5050b8721d113e6e46"

paystack = Paystack(secret_key=SECRET_KEY)



# VERIFY TRANSACTION

url = "https://api.paystack.co/transaction/verify/{reference}"
headers = {
    "Authorization": f"Bearer {SECRET_KEY}",
    "Cache-Control": "no-cache"
}

response = requests.get(url.format(reference="pBCiUf1xwJyEKbv1"), headers=headers)

if response.status_code != 200:
    print(f"Error: {response.status_code}")
else:
    pprint(response.text)


