from home.models import Ledger,Voucher
from django.db import models
from home.models import Firm
TRANSACTION_MODES = (
        ('Cash','Cash'),
        ('Bank','Bank')
    )
TRANSACTION_TYPES = (
        ('Debit','Debit'),
        ('Credit','Credit')
    )
VOUCHER_TYPES = (
        ('Imprest','Imprest'),
        ('Receive','Receive'),
        ('Expense','Expense'),
        ('Journal','Expense'),
        ('Opening','Opening')
    )
class Transaction(models.Model):
    ledger = models.ForeignKey(Ledger, null=False, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=TRANSACTION_TYPES, default="Debit")
    description = models.CharField(max_length=500, default="No description")
    mode = models.CharField(max_length=50, choices=TRANSACTION_MODES, default="Cash")
    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE, null=True,default=-1)
    voucher_type = models.CharField(max_length=50, choices=VOUCHER_TYPES, default="Journal")
    amount = models.FloatField(default=0.0)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    def save(self,*args,**kwargs):
        if self.description == "":
            self.description  = "No description"
        super(Transaction, self).save(*args, **kwargs)

""""
class Expense(models.Model):
    ledger = models.ForeignKey(Ledger,null=False,on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    transaction_type = models.CharField(max_length=50,choices=TRANSACTION_CHOICES,default="Cash")
    voucher = models.ForeignKey(Voucher,on_delete=models.CASCADE,null=True)
    amount_left = models.FloatField(default=0.0)
    description = models.CharField(max_length=500,default="No description")
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

class Impress(models.Model):
    ledger = models.ForeignKey(Ledger, null=False,on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_CHOICES,default="Cash")
    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE,null=True)
    pending = models.BooleanField(default=True)
    amount_left = models.FloatField(default=0.0)
    description = models.CharField(max_length=500, default="No description")
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)



class Receive(models.Model):
    ledger = models.ForeignKey(Ledger, null=False,on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_CHOICES, default="Cash")
    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE,null=True)
    description = models.CharField(max_length=500, default="No description")
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    
"""













