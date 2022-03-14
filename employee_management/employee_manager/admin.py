from django.contrib import admin
from attr import fields
from .models import Employee, ClockIn, EmployeeInstance
# Register your models here.
admin.site.register(Employee)

admin.site.register(EmployeeInstance)
admin.site.register(ClockIn)

