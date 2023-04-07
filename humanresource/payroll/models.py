from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

""" Employee Model: 
#  fields: 
#  first_name, 
#  last_name, email, 
#  phone_number, 
#  hire_date, 
#  job_title,
#  department,
#  manager.
#  These fields define the attributes of an employee such as their name, contact information, hire date, job title, 
#  department, and manager. The phone_number field uses the PhoneNumberField to store a phone number in the Philippine region format. 
#  manager is a foreign key to the Employee model itself, 
#  allowing an employee to have a manager who is also an employee in the same table. """

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = PhoneNumberField(region='PH')
    hire_date = models.DateField()
    job_title = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    manager = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

""" JobTitle Model: 
# title, 
# description. 
# These fields define the attributes of a job title such as the title name and a description of the title. """

class JobTitle(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
