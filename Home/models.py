import uuid
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Expenses(models.Model):
    expense_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    description = models.CharField(max_length=255, null=True)
    expense_date = models.DateField(null=True)
    method_name = models.CharField(max_length=10, null=True)

    def _str_(self):
        return f"Expense {self.expense_id} by {self.user.username}"

class Payment_Method(models.Model):
    payment_id = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    method_name = models.CharField(max_length=10, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense = models.ForeignKey(Expenses, on_delete=models.CASCADE, null=True)

    def _str_(self):
        return f"Expense {self.payment_id} by {self.user.username}"

class Category(models.Model):
    expense_id = models.ForeignKey(Expenses, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=10, null=True)
    def _str_(self):
        return f"Expense {self.category_name }by {self.User.id}"

class Budget(models.Model):
    budget_id = models.AutoField(primary_key=True)
    monthly_limit = models.IntegerField(null=True)
    category_name = models.CharField(max_length=10, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def _str_(self):
        return f"Expense {self.budget_id} by {self.user.username}"



