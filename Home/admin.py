from django.contrib import admin
from .models import Expenses,Payment_Method,Category,Budget

admin.site.register(Expenses)
admin.site.register(Payment_Method)
admin.site.register(Category)
admin.site.register(Budget)