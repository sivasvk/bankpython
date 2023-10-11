# Generated by Django 4.2.2 on 2023-10-10 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0021_person_account_type_person_materials_provide'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='materials_provide',
            new_name='cheque_book',
        ),
        migrations.AddField(
            model_name='person',
            name='credit_card',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='debit_card',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=models.CharField(default='', max_length=10),
        ),
    ]
