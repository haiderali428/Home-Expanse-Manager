from django import forms
from .models import Budget
from datetime import datetime
from .models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'amount', 'description', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['category', 'budget_amount', 'description', 'month']
        widgets = {
            'month': forms.DateInput(attrs={'type': 'date'}),
        }
       