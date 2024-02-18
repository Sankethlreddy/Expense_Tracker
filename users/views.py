from django.shortcuts import render,redirect
from django.contrib import messages
from users.forms import UserRegisterForm



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created successfully for {username}')
            return redirect('Expense-Tracking')
    else:
        form = UserRegisterForm()
        
    return render(request,'users/Signup.html',{'form': form})
