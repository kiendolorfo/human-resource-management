from django.apps import AppConfig

""" PayrollConfig class inherits from AppConfig and 
specifies some configuration options for the "payroll" app."""

class PayrollConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'payroll'
