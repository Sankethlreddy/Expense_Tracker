from django import forms

class Dashboard(forms.Form):
    Amount = forms.IntegerField()
    Date = forms.DateField()
    Payment_Method = forms.ChoiceField(choices=[('cash', 'Cash'), ('card', 'Card'), ('other', 'Other')])
    Category_CHOICES = [
        ('', 'Select a category'),
        ('essentials', 'Essentials'),
        ('lifestyle', 'Lifestyle'),
        ('transportation', 'Transportation'),
        ('savings', 'Savings'),
        ('others', 'Others'),
    ]
    Category = forms.ChoiceField(choices=Category_CHOICES)
    Description = forms.CharField(max_length=300)
