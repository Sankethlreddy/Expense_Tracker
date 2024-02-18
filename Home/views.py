from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return render(request,'Home/Home.html')

def Expense_Tracking(request):
    return render(request,'Home/index.html')

def Budget(request):
    return render(request,'Home/Budget.html')

def Report(request):
    return render(request,'Home/report.html')

def Transactions(request):
    return render(request,'Home/transactions.html')