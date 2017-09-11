
from django import forms
from .models import Ledger


class LedgerForm(forms.ModelForm):
    address = forms.CharField(required=False)
    pan_no = forms.CharField(required=False)
    mobile_no = forms.CharField(required=False)
    class Meta:
        model = Ledger
        fields = ['name', 'address', 'mobile_no', 'pan_no','type']

