from django.contrib import admin
from .models import Expense,Impress,Receive


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ["ledger", "amount", "transaction_type",'voucher']

admin.site.register(Expense,ExpenseAdmin)

class ImpressAdmin(admin.ModelAdmin):
    list_display = ["ledger", "amount", "transaction_type",'voucher',"amount_left"]

admin.site.register(Impress,ImpressAdmin)

class ReceiveAdmin(admin.ModelAdmin):
    list_display = ["ledger", "amount", "transaction_type","voucher"]

admin.site.register(Receive,ReceiveAdmin)