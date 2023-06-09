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

url = "https://api.paystack.co/transaction/2868415249"
headers = {
    "Authorization": f"Bearer {SECRET_KEY}"
}

response = requests.get(url, headers=headers)
print(response.text)