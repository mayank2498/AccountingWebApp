from __future__ import unicode_literals
from firm.models import Firm
from django.db import models

# Create your models here.
class Voucher(models.Model):
    voucher_no = models.CharField(max_length=500)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return str(self.voucher_no)

class Ledger(models.Model):
    LEDGER_TYPE = (
        ('Supplier','Supplier'),
        ('Customer','Customer'),
        ('Employee','Employee'),
    )
    firm = models.ForeignKey(Firm,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=False)
    address = models.CharField(max_length=500)
    mobile_no = models.CharField(max_length=10)
    pan_no = models.CharField(max_length=100)
    type =  models.CharField(max_length=50,choices=LEDGER_TYPE,blank=False,null=False,default='Supplier')
    temp1 = models.FloatField(default=0.0)
    temp2 = models.FloatField(default=0.0)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.name+"  :   "+self.type