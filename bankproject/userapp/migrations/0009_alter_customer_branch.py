# Generated by Django 4.2.2 on 2023-10-02 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0008_alter_customer_account_type_alter_customer_branch_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='branch',
            field=models.CharField(max_length=100),
        ),
    ]
