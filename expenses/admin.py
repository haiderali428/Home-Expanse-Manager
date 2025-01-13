from django.contrib import admin
from .models import Expense, MonthlyBudget

# Register your models here.
admin.site.register(Expense)
admin.site.register(MonthlyBudget)
