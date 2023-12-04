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
    

def create_invoice(amount, tax_id, name, tags):
    invoice = starkbank.invoice.create([
        starkbank.Invoice(
            amount=amount, 
            name=name,
            tax_id=tax_id, 
            tags=["test"],
        )
    ])
    print(invoice)