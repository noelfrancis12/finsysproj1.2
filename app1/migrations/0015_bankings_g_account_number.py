# Generated by Django 3.2.22 on 2023-10-17 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_loan_transaction_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankings_g',
            name='account_number',
            field=models.IntegerField(default=0),
        ),
    ]
