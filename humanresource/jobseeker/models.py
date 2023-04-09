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
    
class EducationLevel(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    
class ExperienceLevel(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class JobSeeker(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = PhoneNumberField(region='PH')
    date_of_birth = models.DateField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    marital_status = models.ForeignKey(MaritalStatus, on_delete=models.CASCADE)
    education_level = models.ForeignKey(EducationLevel, on_delete=models.CASCADE)
    experience_level = models.ForeignKey(ExperienceLevel, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class EducationBackground(models.Model):
    jobseeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False)