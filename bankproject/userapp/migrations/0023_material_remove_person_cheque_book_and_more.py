# Generated by Django 4.2.2 on 2023-10-10 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0022_rename_materials_provide_person_cheque_book_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='cheque_book',
        ),
        migrations.RemoveField(
            model_name='person',
            name='credit_card',
        ),
        migrations.RemoveField(
            model_name='person',
            name='debit_card',
        ),
        migrations.AddField(
            model_name='person',
            name='materials_provide',
            field=models.ManyToManyField(to='userapp.material'),
        ),
    ]
