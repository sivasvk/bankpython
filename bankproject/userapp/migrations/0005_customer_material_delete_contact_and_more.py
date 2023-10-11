# Generated by Django 4.2.2 on 2023-10-02 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_alter_contact_age_alter_contact_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('phone_number', models.CharField(max_length=15)),
                ('mail_id', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('district', models.CharField(choices=[('ernakulam', 'Ernakulam'), ('malappuram', 'Malappuram'), ('kannur', 'Kannur'), ('thrissur', 'Thrissur'), ('kozhikode', 'Kozhikode')], max_length=20)),
                ('branch', models.CharField(blank=True, choices=[], max_length=20)),
                ('account_type', models.CharField(choices=[('savings', 'Savings Account'), ('current', 'Current Account')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.AddField(
            model_name='customer',
            name='materials_provide',
            field=models.ManyToManyField(to='userapp.material'),
        ),
    ]
