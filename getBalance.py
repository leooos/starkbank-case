import starkbank
import os

private_key_content = os.environ.get('private_key_content')
if private_key_content is None:
    from key import private_key_content

starkbank.user = starkbank.Project(
    environment="sandbox",
    id="6278407566393344",
    private_key=private_key_content
)
    

def get_balance():
    balance = starkbank.balance.get()
    return balance