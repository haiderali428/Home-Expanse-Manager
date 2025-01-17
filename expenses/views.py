from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Expense
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from .middlewares import auth
from django.http import HttpResponse
from .forms import BudgetForm
from .models import Budget


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

    expenses_list = Expense.objects.all()
    return render(request, 'expenses.html', {'expenses': expenses_list})

# Reports View
def reports(request):
    expenses = Expense.objects.all()
    return render(request, 'reports.html', {'expenses': expenses})

# Budget View
def budget(request):
    return render(request, 'budget.html')

# Handling Deletion via Ajax (use CSRF token for security)
@csrf_protect
def delete_expense(request, expense_id):
    if request.method == 'DELETE':
        try:
            expense = Expense.objects.get(id=expense_id)
            expense.delete()
            return JsonResponse({'success': True})
        except Expense.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Expense not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})
def add_expense(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        date = request.POST.get('date')

        # Save to database
        Expense.objects.create(
            category=category,
            description=description,
            amount=amount,
            date=date
        )

        return HttpResponse("Expense added successfully!")
    return render(request, 'add_expense.html')  # Render a form template
def budget_submission(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally, redirect to avoid form resubmission
            # return redirect('some_view')
        else:
            print(form.errors) 
            print(form.cleaned_data)
    else:
        form = BudgetForm()
    
    # Get all the budgets from the database
    budgets = Budget.objects.all()
    
    return render(request, 'expenses.html', {'budgets': budgets})
