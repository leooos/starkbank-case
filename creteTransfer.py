import starkbank

private_key_content = """
-----BEGIN EC PRIVATE KEY-----
MHQCAQEEINopt+q6XkVIJ8Lnad56veOSNr9Uj+4kOzyZgEXuoNVtoAcGBSuBBAAK
oUQDQgAE9SjYJErMoUTHietJFWjiGsC+wFveMxW2uE89G7WiLrUJO9R+nHeE1Yj6
mWKb/MpFKlzYbdtwLh4wzkNLxlnGtQ==
-----END EC PRIVATE KEY-----
"""

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