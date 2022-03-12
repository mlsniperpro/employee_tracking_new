from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    role = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name+' '+self.last_name}"
