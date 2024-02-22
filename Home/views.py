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
    if request.method == "POST":
        user_instance = request.user
        essentials_budget = request.POST.get('essentials-budget', '')
        if essentials_budget != '':
            user_budget = models.Budget(user=user_instance, monthly_limit=essentials_budget, category_name='Essentials')
            user_budget.save()
        lifeStyle_budget = request.POST.get('lifestyle-budget', '')
        if lifeStyle_budget != '':
            user_budget = models.Budget(user=user_instance, monthly_limit=lifeStyle_budget, category_name='Lifestyle')
            user_budget.save()
        Transportation_budget = request.POST.get('transportation-budget', '')
        if Transportation_budget != '':
            user_budget = models.Budget(user=user_instance, monthly_limit=Transportation_budget, category_name='Transportation')
            user_budget.save()
        savings_budget= request.POST.get('savings-budget', '')
        if savings_budget != '':
            user_budget = models.Budget(user=user_instance, monthly_limit=savings_budget, category_name='Savings')
            user_budget.save()
        return HttpResponse('Data Successfully Stored')
    return render(request, 'Home/Budget.html')
def Report(request):
    return render(request,'Home/report.html')

def Transactions(request):
    return render(request,'Home/transactions.html')