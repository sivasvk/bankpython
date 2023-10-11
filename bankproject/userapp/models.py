from sre_parse import Verbose
from django.db import models


class Person(models.Model):

    ACCOUNT_TYPE_CHOICES = [
        ('Savings', 'Savings Account'),
        ('Checking', 'Checking Account'),
        ('Investment', 'Investment Account')
    ]


    name = models.CharField(max_length=100)
    dob = models.DateField(blank=True, null=True)
    age = models.PositiveIntegerField(default='')
    gender = models.CharField(max_length=10, default='', choices=(('male', 'Male'), ('female', 'Female')))
    phone_number = models.CharField(max_length=10,default='')
    mail_id = models.EmailField(default='')
    address = models.TextField(blank=True, null=True)
    district = models.ForeignKey('District', on_delete=models.CASCADE)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)
    account_type = models.CharField(max_length=20,default='', choices=ACCOUNT_TYPE_CHOICES)
    materials_provide = models.ManyToManyField('Material')
    
    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    

class Branch(models.Model):
    name = models.CharField(max_length=15)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Material(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name    