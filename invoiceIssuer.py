import random
import starkbank
#import time
#import schedule
import datetime

from createPerson import create_person
from createInvoice import create_invoice
from apscheduler.schedulers.blocking import BlockingScheduler

def issue_invoices():
    print("rodou as "+ str(datetime.datetime.now()))        
    invoices= random.randint(8, 12)
    payers= create_person(invoices)

    for payer in payers:
        amount=payer['amount']
        name=payer['name']
        tax_id=payer['tax_id'] 
        tags=["test"]
        create_invoice(amount=amount, name=name, tax_id=tax_id, tags=tags)  

sched = BlockingScheduler()
issue_invoices()
@sched.scheduled_job('interval', hours=3)
def timed_job():
    issue_invoices()

sched.start()