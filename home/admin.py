from django.contrib import admin
from .models import Ledger,Voucher

# Register your models here.

class LedgerAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "type", "pan_no", "mobile_no","firm"]

admin.site.register(Ledger,LedgerAdmin)

class VoucherAdmin(admin.ModelAdmin):
    list_display = ["voucher_no","created"]

admin.site.register(Voucher,VoucherAdmin)