
from django import forms
from .models import Firm


class FirmForm(forms.ModelForm):
    class Meta:
        model = Firm
        fields = ['name', 'year']

