from django.shortcuts import render
from .models import Employee, EmployeeInstance, ClockIn, ClockOut
from django.views import generic

#Create your views here
def index(request):
    """Our view function for the homepage of the site"""

    #Generating essential object counts
    num_of_employees = Employee.objects.all().count()
    num_instances = EmployeeInstance.objects.all().count()

    #Available employees (status = 'a')
    num_instances_available = EmployeeInstance.objects.filter(status__exact='a').count()
    employees_on_leave = EmployeeInstance.objects.filter(status__exact='b').count()
    #all() is implied
    employees_who_reported = ClockIn.objects.count()
    employees_who_left = ClockOut.objects.count()
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits+1
    context = {
        'num_of_employees':num_of_employees,
        'num_instances':num_instances,
        'num_instances_available':num_instances_available,
        'employees_who_reported':employees_who_reported,
        'employees_who_left':employees_who_left,
        'employees_on_leave':employees_on_leave,
        'num_visits': num_visits,
    } 

    #Render the HTML template below index.html with data in context variable
    return render(request, 'index.html', context=context)
class EmployeeListView(generic.ListView):
    model = Employee
    paginate_by = 10
class EmployeeDetailView(generic.DetailView):
    model = Employee
