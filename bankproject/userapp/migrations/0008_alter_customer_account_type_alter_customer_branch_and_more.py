# Generated by Django 4.2.2 on 2023-10-02 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0007_remove_customer_materials_provide_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='account_type',
            field=models.CharField(choices=[('savings', 'Savings Account'), ('current', 'Current Account')], max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='branch',
            field=models.CharField(blank=True, choices=[], max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='district',
            field=models.CharField(choices=[('ernakulam', 'Ernakulam'), ('malappuram', 'Malappuram'), ('kannur', 'Kannur'), ('thrissur', 'Thrissur'), ('kozhikode', 'Kozhikode')], max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
    ]
