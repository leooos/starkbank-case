import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/invoice', methods=['POST'])
def webhook_receiver():
    data = request.json
    print(data)
    return '', 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
