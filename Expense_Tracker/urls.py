"""
URL configuration for Expense_Tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from users import views as user_views
from Home import views as Home_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("Home.urls")),
    path('Expense_Tracking/', Home_views.Expense_Tracking, name='Expense-Tracking'),
    path('register/',user_views.register , name ='register'),
    path('login/',auth_views.LoginView.as_view(template_name = 'users/login.html') , name ='login'),
    path('Expense_Tracking/logout/',user_views.custom_logout , name ='logout'),
]
