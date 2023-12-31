import os
from flask import Flask, request

from creteTransfer import create_transfer

app = Flask(__name__)
@app.route('/invoice', methods=['POST'])
def webhook_receiver():
    data = request.json
    if "event" not in data:
        return 'error', 400
    print(data["event"]["log"]["type"])

    if data["event"]["log"]["type"] == "credited":
        print("create transfer")
        amount = data["event"]["log"]["invoice"]["amount"]
        bank_code = "20018183"
        branch_code = "0001"
        account_number = "6341320293482496"
        account_type = "payment"
        tax_id = "20.018.183/0001-80"
        name = "Stark Bank S.A."
        tags = ["case"]
        create_transfer(amount,bank_code, branch_code, account_number, account_type, tax_id, name, tags)    

    return 'POST ok', 200

@app.route('/', methods=['GET'])
def get_receiver():
    return 'Status ativo', 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)