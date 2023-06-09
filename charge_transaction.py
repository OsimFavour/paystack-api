import random
import string
import requests
from paystackapi.paystack import Paystack
from paystackapi.plan import Plan
from paystackapi.transaction import Transaction

EMAIL = "famos204@gmail.com"

SECRET_KEY = "sk_test_4f188e63dc16982fc116eb5050b8721d113e6e46"

paystack = Paystack(secret_key=SECRET_KEY)


# CHARGE TRANSACTION

charge_response = Transaction.charge(
    reference=''.join(
            [random.choice(
                string.ascii_letters + string.digits) for n in range(16)]),
    authorization_code="AUTH_wyvxszlnj8",
    email=EMAIL,
    amount="50000"
)

print(charge_response)


# CHARGE TRANSACTION API

# url = "https://api.paystack.co/transaction/charge_authorization"
# headers = {
#     "Authorization": f"Bearer {SECRET_KEY}",
#     "Content-Type": "application/json"
# }

# data = {
#     "email": "famos204@gmail.com",
#     "amount": "50000",
#     "authorization_code": "AUTH_wyvxszlnj8"
# }

# response = requests.post(url, headers=headers, json=data)
# print(response.text)
