from django.db import models
from datetime import datetime

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('groceries', 'Groceries'),
        ('rent', 'Rent'),
        ('utilities', 'Utilities'),
        ('entertainment', 'Entertainment'),
        ('savings', 'Savings'),
    ]
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    def __str__(self):
        return f"{self.category} expense of {self.amount} on {self.date}"

class MonthlyBudget(models.Model):
    CATEGORY_CHOICES = [
        ('groceries', 'Groceries'),
        ('rent', 'Rent'),
        ('utilities', 'Utilities'),
        ('entertainment', 'Entertainment'),
        ('savings', 'Savings'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    budget_amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.DateField()

    def __str__(self):
        return f"{self.get_category_display()} - {self.budget_amount} for {self.month.strftime('%B %Y')}"

    class Meta:
        ordering = ['-month']  # Order by month descending

class Budget(models.Model):
    CATEGORY_CHOICES = [
        ('grocerries', 'Groceries'),
        ('rent', 'Rent'),
        ('utilities', 'Utilities'),
        ('entertainment', 'Entertainment'),
        ('savings', 'Savings'),
    ]
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    budget_amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    month = models.DateField()

    def __str__(self):
        return f'{self.category} budget for {self.month.strftime("%B %Y")}'
