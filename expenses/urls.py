from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Default route for index.html
    path('index', views.index, name='index'),  # Default route for index.html
     path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('expenses', views.expenses, name='expenses'),
    path('budget', views.budget, name='budget'),
    path('reports', views.reports, name='reports'),
     path('delete-expense/<int:expense_id>/', views.delete_expense, name='delete_expense'),
         path('add-expense/', views.add_expense, name='add_expense'),
 path('submit_budget/', views.budget_submission, name='budget_submission'), 
 path('expense/add/', views.expense_submission, name='expense_submission'),]