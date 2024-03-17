import uuid
from django.shortcuts import redirect, render
from django.http import HttpResponse
from datetime import datetime

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


        #displaying total expense
    #expenses = total_expense()
    user_instance  = request.user
    t_expense = 0
    datas = models.Expenses.objects.all()
    #datas = models.Expenses.objects.all().values_list('user','amount')
    data_list =list(datas)

    for data in data_list :
        if user_instance == data.user:
            t_expense = int(data.amount) + t_expense

    
    #cat_expense
    e_a=0
    l_a=0
    t_a=0
    s_a=0

    for data in data_list :
        if user_instance == data.user:
            if data.category_name ==  "essentials":
                e_a = data.amount + e_a
            elif data.category_name ==  "lifestyle":
                l_a = data.amount+ l_a
            elif data.category_name ==  "transportation":
                t_a = data.amount+ t_a
            elif data.category_name ==  "savings":
                s_a = data.amount + s_a
    
    #Budget remaining
    b_datas = models.Budget.objects.all()
    b_data_list = list(b_datas)
    e_b=0
    l_b=0
    t_b=0
    s_b=0

    
    ##getting the monthly lmits
    
    for b_data in b_data_list :
        if user_instance == b_data.user:
            if b_data.category_name ==  "Essentials":
                e_b = b_data.monthly_limit
            elif b_data.category_name ==  "Lifestyle":
                l_b = b_data.monthly_limit
            elif b_data.category_name ==  "Transportation":
                t_b = b_data.monthly_limit
            elif b_data.category_name ==  "Savings":
                s_b = b_data.monthly_limit

    

    e_br= e_b-e_a
    l_br= l_b-l_a
    t_br= t_b-t_a
    s_br= s_b-s_a

    #rem_list=[e_br,l_br,t_br,s_br]
    return render(request,'Home/index.html',{'t_expense':t_expense,'e_br':e_br,'l_br': l_br,'t_br':t_br,'s_br':s_br})

    

    


def Budget(request):
    null = ""
    if request.method == "POST":
        user_instance = request.user
        essentials_budget = request.POST.get('essentials-budget', '')
        if essentials_budget != '':
            if str(models.Budget.objects.filter(user=user_instance,category_name='Essentials')) == "<QuerySet []>":
                user_budget = models.Budget(user=user_instance, monthly_limit=essentials_budget, category_name='Essentials')
                user_budget.save()
            else:
                models.Budget.objects.filter(user=user_instance,category_name='Essentials').update(monthly_limit=essentials_budget)           
                
        lifeStyle_budget = request.POST.get('lifestyle-budget', '')
        if lifeStyle_budget != '':
            if str(models.Budget.objects.filter(user=user_instance,category_name='Lifestyle')) == "<QuerySet []>":
                user_budget = models.Budget(user=user_instance, monthly_limit=lifeStyle_budget, category_name='Lifestyle')
                user_budget.save()
            else:
                models.Budget.objects.filter(user=user_instance,category_name='Lifestyle').update(monthly_limit=lifeStyle_budget)
                
        Transportation_budget = request.POST.get('transportation-budget', '')
        if Transportation_budget != '':
            if str(models.Budget.objects.filter(user=user_instance,category_name='Transportation')) == "<QuerySet []>":
                user_budget = models.Budget(user=user_instance, monthly_limit=Transportation_budget, category_name='Transportation')
                user_budget.save()
            else:
                models.Budget.objects.filter(user=user_instance,category_name='Transportation').update(monthly_limit=Transportation_budget)
                
        savings_budget= request.POST.get('savings-budget', '')
        if savings_budget != '':
            if str(models.Budget.objects.filter(user=user_instance,category_name='Savings')) == "<QuerySet []>":
                user_budget = models.Budget(user=user_instance, monthly_limit=savings_budget, category_name='Savings')
                user_budget.save()
            else:
                models.Budget.objects.filter(user=user_instance,category_name='Savings').update(monthly_limit=savings_budget)
                
        HttpResponse('Data Successfully Stored')
    return render(request, 'Home/Budget.html')
def Report(request):
    
    
    #displaying total expense
    user_instance  = request.user
    t_expense = 0
    datas = models.Expenses.objects.all()
    #datas = models.Expenses.objects.all().values_list('user','amount')
    data_list =list(datas)

    for data in data_list :
        if user_instance == data.user:
            t_expense = int(data.amount) + t_expense

    return render(request,'Home/report.html',{'t_expense':t_expense})

def Transactions(request):
    user_instance  = request.user
    
    
    essential_objs =models.Expenses.objects.filter(user=user_instance)
    # lifestyle_obj =models.Expenses.objects.filter(user=user_instance,category_name='lifestyle')
    # Transportation_obj =models.Expenses.objects.filter(user=user_instance,category_name='transportation')
    # savings_obj =models.Expenses.objects.filter(user=user_instance,category_name='savings')








    return render(request,'Home/transactions.html',{'essential_objs':essential_objs})

# from django.shortcuts import redirect

# def Logout(request):
#     return render(request,'User/logout.html')
