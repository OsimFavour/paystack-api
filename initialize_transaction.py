import random
import string
import requests
from paystackapi.paystack import Paystack
from paystackapi.plan import Plan
from paystackapi.transaction import Transaction

EMAIL = "famos204@gmail.com"

SECRET_KEY = "sk_test_4f188e63dc16982fc116eb5050b8721d113e6e46"

paystack = Paystack(secret_key=SECRET_KEY)


# INITIALIZE TRANSACTION

reference = ''.join(
            [random.choice(
                string.ascii_letters + string.digits) for n in range(16)])
print(reference)

init_response = Transaction.initialize(
    reference=reference,
    amount="20000",
    email=EMAIL,
    plan="PLN_hdfpemllr392zpj"
)

print(init_response)


# USE INITIALIZE API


# url = "https://api.paystack.co/transaction/initialize"
# headers = {
#     "Authorization": f"Bearer {SECRET_KEY}",
#     "Cache-Control": "no-cache"
# }

# data = {
#     'email': "famos204@gmail.com",
#     'amount': "10000",
# }

# response = requests.post(url, headers=headers, data=data)
# print(response.text)