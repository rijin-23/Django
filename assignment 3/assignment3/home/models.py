from django.db import models

# Create your models here.
class Information(models.Model):
    user_name =  models.CharField(max_length=30)
    password =  models.CharField(max_length=30)
    phone_number =  models.CharField(max_length=10)
    address = models.CharField(max_length=50)