from django.contrib import admin
from attr import fields
from .models import Employee, ClockIn, EmployeeInstance, ClockOut
# Register your models here.
#admin.site.register(Employee)
class EmployeeInstanceInline(admin.TabularInline):
    model = EmployeeInstance
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    look_display = ('first_name', 'last_name','email','department','role')

    inlines = [EmployeeInstanceInline]
#admin.site.register(EmployeeInstance)
@admin.register(EmployeeInstance)
class EmployeeInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status','end_date')
    fieldsets = (
        (None, {
            'fields':('employee','off_reason','id')
        }),
        ('Availalability',{
            'fields':('status','end_date')
        }),
    )
admin.site.register(ClockIn)
admin.site.register(ClockOut)

