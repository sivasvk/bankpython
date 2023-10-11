# Generated by Django 4.2.2 on 2023-10-02 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0006_rename_name_customer_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='materials_provide',
        ),
        migrations.AddField(
            model_name='customer',
            name='materials_provided',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.DeleteModel(
            name='Material',
        ),
    ]
