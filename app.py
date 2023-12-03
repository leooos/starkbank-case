import os
from flask import Flask, request

from creteTransfer import create_transfer
app = Flask(__name__)

@app.route('/invoice', methods=['POST'])
def webhook_receiver():
    data = request.json
    
    if data["event"]["log"]["type"] == "credited":
        print("create transfer")
        amount = data["event"]["log"]["invoice"]["amount"]
        bank_code="00655522",
        branch_code="0001",
        account_number="10000-0",
        account_type="salary",
        tax_id="386.331.928-10",
        name="Domonique Whisenhunt",
        tags=["tests"]
        #bank_code= "20018183"
        #branch_code= "0001"
        #account_number= "6341320293482496"
        #account_type= "payment"
        #tax_id= "20.018.183/0001-80"
        #name= "Stark Bank S.A."
        create_transfer(amount,bank_code, branch_code, account_number, account_type, tax_id, name, tags)
        print("----")
        print(data)

    return '', 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)