# Generated by Django 5.0.2 on 2024-02-22 04:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Home', '0004_remove_category_expense_id_remove_expenses_id_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('budget_id', models.AutoField(primary_key=True, serialize=False)),
                ('monthly_limit', models.IntegerField(null=True)),
                ('category_name', models.CharField(max_length=10, null=True)),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('expense_id', models.IntegerField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=255, null=True)),
                ('expense_date', models.DateField(null=True)),
                ('method_name', models.CharField(max_length=10, null=True)),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=10, null=True)),
                ('expense_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.expenses')),
            ],
        ),
        migrations.CreateModel(
            name='Payment_Method',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('method_name', models.CharField(max_length=10, null=True)),
                ('expense', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.expenses')),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
