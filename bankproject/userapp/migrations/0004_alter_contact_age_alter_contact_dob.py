# Generated by Django 4.2.2 on 2023-09-28 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_alter_contact_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]