from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Expense, MonthlyBudget
from django.contrib import messages

from .middlewares import auth, guest

# Views

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')
# Index View
@auth
def index(request):
    return render(request, 'index.html')

# Expenses View

def expenses(request):
    if request.method == 'POST':
        try:
            # Create a new expense entry in the database
            Expense.objects.create(
                category=request.POST.get('budgetCategory'),
                description=request.POST.get('budgetDescription'),
                amount=request.POST.get('budgetAmount'),
                date=request.POST.get('budgetDate'),
            )
            messages.success(request, "Expense has been added successfully.")
        except Exception as e:
            messages.error(request, f"Error adding expense: {str(e)}")
        return redirect('expenses')

    # Display all expenses
    expenses_list = Expense.objects.all()
    return render(request, 'expenses.html', {'expenses': expenses_list})

# Reports View

def reports(request):
    expenses = Expense.objects.all()
    return render(request, 'reports.html', {'expenses': expenses})

# Budget View

def budget(request):
    return render(request, 'budget.html')
