from django.shortcuts import render
from django.http import HttpResponse

from .forms import Dashboard

def Home(request):
    return render(request,'Home/Home.html')

def Expense_Tracking(request):
    form = Dashboard(request.POST)
    if request.method == "POST":
        form.save
        if form.is_valid():
            Amount = form.cleaned_data.get('Amount')
    return render(request,'Home/index.html',{'form': form})

def Budget(request):
    return render(request,'Home/Budget.html')

def Report(request):
    return render(request,'Home/report.html')

def Transactions(request):
    return render(request,'Home/transactions.html')