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
    

def create_transfer(amount, bank_code, branch_code, account_number, account_type, tax_id, name, tags):
    transfer = starkbank.transfer.create([
        starkbank.Transfer(
            amount=amount,
            bank_code=bank_code,
            branch_code=branch_code,
            account_number=account_number,
            account_type=account_type,
            tax_id=tax_id,
            name=name,
            tags=tags
        )
    ])
    print(transfer)