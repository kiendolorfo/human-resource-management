from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = PhoneNumberField(region='PH')
    hire_date = models.DateField()
    job_title = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"