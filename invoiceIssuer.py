import random
import starkbank
import time
import schedule
import datetime

from createPerson import create_person
from createInvoice import create_invoice
from apscheduler.schedulers.blocking import BlockingScheduler

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
          

sched = BlockingScheduler()
testar()
@sched.scheduled_job('interval', minutes=1)
def timed_job():
    i=+1
    testar()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

sched.start()