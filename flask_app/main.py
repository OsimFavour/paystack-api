import random
import string
import requests
import time
from flask import Flask, render_template, redirect, url_for, flash, abort, request, session
from paystackapi.transaction import Transaction
from paystackapi.paystack import Paystack
from paystack.resource import TransactionResource


app = Flask(__name__)
app.app_context().push()
app.config["SECRET_KEY"] = "kdwepd843jfkc40oke0342cmcor04kmdrmformf0303ed30kd"

SECRET_KEY = "sk_test_4f188e63dc16982fc116eb5050b8721d113e6e46"

        

def paystack_client(reference, amount):
    Paystack(secret_key=SECRET_KEY)
    client = Transaction.initialize(
            reference=reference, 
            amount=amount,
            email="famos204@gmail.com")
    return client


def get_transaction():
    Paystack(secret_key=SECRET_KEY)

    response = Transaction.get(transaction_id=2868648008)

    return response


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method=="POST":

        SECRET_KEY = "sk_test_4f188e63dc16982fc116eb5050b8721d113e6e46"

        Paystack(secret_key=SECRET_KEY)
        amount = request.form.get("amount")
        # print(f"Amount: {amount}")
        email = request.form.get("email")
        print(email)
        
         
        rand = ''.join(
            [random.choice(
                string.ascii_letters + string.digits) for n in range(16)])
        secret_key = 'sk_test_4f188e63dc16982fc116eb5050b8721d113e6e46'
        reference = rand
        test_email = email
        # test_amount = '100'
        plan = 'PLN_hdfpemllr392zpj'
        callback_url = "http://127.0.0.1:4000/payment-callback"
        
        # client = paystack_client(reference, amount)
        # print(client)

        client = TransactionResource(secret_key, reference)
        response = client.initialize(amount,
                                    test_email)
        print(response)

        

        session["response"] = response
        # session["client_data"] = client.get("data", {})
        # print(client.get("data", {}))
        if "authorization_url" in response.get("data", {}):
            client.authorize()
            
            # authorization_url = client["data"]["authorization_url"]
            # print("Authorization URL:", authorization_url)
            return redirect(url_for("payment_callback"))
            
            # Redirect the user to the authorization_url to enter card details
        #     return redirect(authorization_url)
        # else:
        #     error_message = client.get("message", "Payment initialization failed.")
        #     print(error_message, "error")
            # return redirect(url_for("home"))
    return render_template("index.html")


def verify_user(reference):
    url = f"https://api.paystack.co/transaction/verify/{reference}"
    headers = {
    "Authorization": f"Bearer {SECRET_KEY}",
    "Cache-Control": "no-cache"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return f"Error: {response.status_code}"
    else:
        return response.json()
    

@app.route("/callback")
def payment_callback():
    time.sleep(30)
    response = session.get("response")
    print(f"Transaction Client: {response}")
    # client_data = session.get("client_data")
    # response = request.get_json()
    # print(f"Clientele: {client_data}")
    status = response["status"]
    reference = response["data"]["reference"]
    print(reference)

    if status == True:
        verified_user = verify_user(reference)
        print(verified_user)
        # verified_user["data"]["reference"]
        amount = verified_user["data"]["amount"]
        print(amount)
        date_paid = verified_user["data"]["paid_at"].split("T")[0]
        print(date_paid)
        time_paid = verified_user["data"]["paid_at"].split("T")[1].split(".")[0]
        print(time_paid)
        authorization_code = verified_user["data"]["authorization"]["authorization_code"]
        print(authorization_code)
        return redirect(url_for('home'))
    
        # Handle the case when payment status is not "success"
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000, debug=True)

