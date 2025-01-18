from django.contrib import admin
from .models import Expense, MonthlyBudget
from .models import Budget


# Register your models here.
admin.site.register(Expense)
admin.site.register(MonthlyBudget)
admin.site.register(Budget)
