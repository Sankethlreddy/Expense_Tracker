import uuid
from django.shortcuts import redirect, render
from django.http import HttpResponse

from Home import models

from .forms import Dashboard

def Home(request):
    return render(request,'Home/Home.html')

def Expense_Tracking(request):
    if request.method == "POST":
        user_instance  = request.user
        expense_id = str(uuid.uuid4())
        Amount = request.POST['expense-amount']
        category = request.POST['category']
        Date = request.POST['expense-date']
        Payment_method = request.POST['method']
        description = request.POST['expense-note']
        user_expenses = models.Expenses(user = user_instance ,amount = Amount ,expense_id =expense_id, category_name=category , expense_date = Date , method_name=Payment_method,description=description)
        user_expenses.save()
        return redirect('Expense-Tracking')
    return render(request,'Home/index.html')


def Budget(request):
    return render(request,'Home/Budget.html')

def Report(request):
    return render(request,'Home/report.html')

def Transactions(request):
    return render(request,'Home/transactions.html')