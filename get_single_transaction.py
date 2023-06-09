from paystackapi.paystack import Paystack
from paystackapi.transaction import Transaction

SECRET_KEY = "sk_test_4f188e63dc16982fc116eb5050b8721d113e6e46"

paystack = Paystack(secret_key=SECRET_KEY)

response = Transaction.get(transaction_id=2868648008)

print(response)