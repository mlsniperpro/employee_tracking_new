from django.db import models
import uuid
from django.utils import timezone
from django.urls import reverse
from sqlalchemy import ForeignKey

# Create your models here.
class Employee(models.Model):
    """Model representing an employee of a company"""
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    joining_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']
    def get_absolute_url(self):
        return reverse("employee-detail", args=[str(self.id)])
    
    def __str__(self):
        return f"{self.first_name}, {self.last_name}"
class ClockIn(models.Model):
    """Model representing the clock in and clock out of employees"""
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, help_text="Unique Id for clocking In")
    clock_in_time = models.DateTimeField(null=True,blank=True)
    employee = ForeignKey('Employee', on_delete=models.RESTRICT,null=True)

class ClockOut(models.Model):
    """Model representing employees Clocking Out"""
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, help_text="Unique Id for clocking Out")
    employee = ForeignKey('Employee', on_delete=models.RESTRICT,null=True)
    clock_out_time = models.DateTimeField(null=True,blank=True)
class EmployeeInstance(models.Model):
    """This represents specific instance of employee(who can be given time off)"""
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, help_text="Unique Id for employee across organization")
    employee = models.ForeignKey('Employee', on_delete=models.RESTRICT,null=True)
    off_reason = models.CharField(max_length=200)
    start_date = models.DateField('OffStarted',null=True,blank=True)
    end_date = models.DateField('OffEnded', null=True,blank=True)
    AVALABILITY_STATUS = (
        ('a','Available'),
        ('b','Off')
    )
    class Meta:
        ordering = ['start_date','end_date']
    def get_absolute_url(self):
        return reverse("time_off", args=[str(self.id)])
    def __str__(self):
        """String representing the time off object"""
        return f'{self.start_date}, {self.end_date}'
    
    
