from unicodedata import name
from django.urls import path

from .import views

urlpatterns = [
     path("", views.index, name="index"),
     path('<int:employee_id>/', views.employee_details, name="employee_details"),
     path('<int:employee_id>/clock_in/', views.clock_in, name="clock_in"),
]
