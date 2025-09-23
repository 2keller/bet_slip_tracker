from django import forms
from .models import Betslip

class BetslipForm(forms.ModelForm):
    class Meta:
        model = Betslip
        fields = ['slip_code', 'bookmaker', 'status', 'checked_at']
        