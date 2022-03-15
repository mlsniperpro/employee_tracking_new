from unicodedata import name
from django.urls import path, include

from .import views

urlpatterns = [
     path('', views.index, name='index'),
     path('employees/', views.EmployeeListView.as_view(),name='employees'),
     path('employee/<int:pk>',views.EmployeeDetailView.as_view(),name='employee-detail'),
     path('offperiods/',views.OffPeriodEmployeesByUserListView.as_view(),name='my-off-periods'),
]
