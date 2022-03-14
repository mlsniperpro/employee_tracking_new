from re import template
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from employee_manager.models import Employee

# Create your views here.
#Here goes the home page
def index(request):
    
    return render(request, "employee_manager/employee_details.html")
def employee_details(request, employee_id):
    employee = get_object_or_404(Employee,pk=employee_id)
    return render(request, "employee_manager/employee_details.html",{'employee':employee})
def clock_in(request, employee_id):
    response = "The employee %s have just clocked in"
    return HttpResponse(response % employee_id)