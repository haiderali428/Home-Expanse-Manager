from django import forms
from .models import Budget
from datetime import datetime
class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['category', 'budget_amount', 'description', 'month']
        widgets = {
            'month': forms.DateInput(attrs={'type': 'date'}),
        }