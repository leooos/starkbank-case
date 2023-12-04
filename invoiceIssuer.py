import random
import starkbank
import time
import schedule
import datetime

from createPerson import create_person
from createInvoice import create_invoice

i=0
def issue_invoices():
    invoices= random.randint(8, 12)
    payers= create_person(invoices)

    for payer in payers:
        amount=payer['amount']
        name=payer['name']
        tax_id=payer['tax_id'] 
        tags=["test"]
        create_invoice(amount=amount, name=name, tax_id=tax_id, tags=tags)

def testar():
    print("rodou as "+ str(datetime.datetime.now()))
    print(i)
          
schedule.every(1).minutes.do(testar)
testar()
while i <= 8: # 8 iterações * 3 horas = 24 horas
    schedule.run_pending()
    time.sleep(60)  # Espera 1 hora (3600 segundos) antes de verificar novamente
    i+=1

print("Fim do período de 24 minutos.")
