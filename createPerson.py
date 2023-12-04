import random

from faker import Faker
from cpf_generator import CPF

def create_person(counter):
    payers = []
    for _ in range(counter):
        amount = random.randint(5000, 100000)
        fake = Faker()
        nome = fake.name()
        tax_id = CPF.generate()

        person = {
            'amount': amount,
            'name': nome,
            'tax_id': tax_id
        }
        payers.append(person)
    return payers