from paystackapi.paystack import Paystack
from paystackapi.plan import Plan

EMAIL = "famos204@gmail.com"

SECRET_KEY = "sk_test_4f188e63dc16982fc116eb5050b8721d113e6e46"

paystack = Paystack(secret_key=SECRET_KEY)


# CREATE PLAN
# N/B: 10,000 kobo is equivalent to 100 Naira 
response = Plan.create(
    name="Freestyle",
    description="Learning the ropes",
    amount="10000",
    interval="daily",
    send_invoices=False,
    currency="NGN"
)

print(response)