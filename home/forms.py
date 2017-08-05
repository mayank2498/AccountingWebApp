
from django import forms
from .models import Ledger


class LedgerForm(forms.ModelForm):

    class Meta:
        model = Ledger
        fields = ['name', 'address', 'mobile_no', 'pan_no','type']

