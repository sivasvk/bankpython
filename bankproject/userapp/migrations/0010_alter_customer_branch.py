# Generated by Django 4.2.2 on 2023-10-02 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0009_alter_customer_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='branch',
            field=models.CharField(blank=True, choices=[], max_length=100),
        ),
    ]