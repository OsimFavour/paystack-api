import random
import string
from flask import Flask, render_template, redirect, url_for, flash, abort, request, session
from paystackapi.transaction import Transaction
from paystackapi.paystack import Paystack

app = Flask(__name__)
app.app_context().push()
app.config["SECRET_KEY"] = "kdwepd843jfkc40oke0342cmcor04kmdrmformf0303ed30kd"

SECRET_KEY = "sk_test_4f188e63dc16982fc116eb5050b8721d113e6e46"

# def paystack_client(reference, amount):
#     Paystack(secret_key=SECRET_KEY)
#     client = Transaction.initialize(
#             reference=reference, 
#             amount=amount,
#             email="famos204@gmail.com")
#     return client


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        amount = request.form.get("amount")
        email = request.form.get("email")
        
        rand = ''.join(
            [random.choice(
                string.ascii_letters + string.digits) for n in range(16)])
        reference = rand

        Paystack(secret_key=SECRET_KEY)
        client = Transaction.initialize(
                reference=reference, 
                amount=amount,
                email="famos204@gmail.com")
        
        # client = paystack_client(reference, amount)
        session["client"] = client
        session["client_data"] = client.get("data", {})
        # print(f"Client Data: {client.get('data', {})}")
        
        if "authorization_url" in client.get("data", {}):
            authorization_url = client["data"]["authorization_url"]
            print(authorization_url)
            return redirect(url_for("payment_redirect"))
        else:
            error_message = client.get("message", "Payment initialization failed.")
            print(error_message, "error")
            # Handle the error
        
    return render_template("index.html")


@app.route("/payment-redirect")
def payment_redirect():
    # client = session.get("client")
    # print(f"Transaction Client: {client}")
    client_data = session.get("client_data")
    # print(f"Payment Redirect: {client_data}")
    authorization_url = client_data.get("authorization_url")
    
    if authorization_url:
        return redirect(authorization_url)
    else:
        # Handle the case when authorization_url is not present
        return redirect(url_for("home"))
    

@app.route("/callback", methods=["GET", "POST"])
def payment_callback():
    client = session.get("client")
    print(f"Transaction Client: {client}")
    client_data = session.get("client_data")
    print(f"Payment Callback: {client_data}")
    status = client["data"]["status"]
    reference = client_data["reference"]

    if status == "True":
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000, debug=True)
