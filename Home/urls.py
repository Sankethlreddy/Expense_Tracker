from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name = "Home"),
    path("Expense_Tracking/", views.Expense_Tracking, name = "Expense-Tracking"),
    path("Expense_Tracking/Budget/", views.Budget, name = "Budget"),
    path("Expense_Tracking/Report/", views.Report, name = "Report"),
    path("Expense_Tracking/Transactions/", views.Transactions, name = "Transactions"),
]
