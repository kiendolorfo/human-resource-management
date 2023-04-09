from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Gender(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    
class MaritalStatus(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class JobSeeker(models.Model):
    MARITAL_STATUS_CHOICES = [
        ('S', 'Single'),
        ('M', 'Married'),
        ('W', 'Widowed'),
        ('D', 'Divorced'),
    ]
    EDUCATION_LEVEL_CHOICES = [
        ('HS', 'High School'),
        ('CL', 'College'),
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
    ]
    EXPERIENCE_LEVEL_CHOICES = [
        ('0-1', '0-1 years'),
        ('1-2', '1-2 years'),
        ('2-3', '2-3 years'),
        ('3-5', '3-5 years'),
        ('5+', '5+ years'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = PhoneNumberField(region='PH')
    date_of_birth = models.DateField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    marital_status = models.ForeignKey(MaritalStatus, on_delete=models.CASCADE)
    education_level = models.CharField(max_length=2, choices=EDUCATION_LEVEL_CHOICES)
    experience_level = models.CharField(max_length=3, choices=EXPERIENCE_LEVEL_CHOICES)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
