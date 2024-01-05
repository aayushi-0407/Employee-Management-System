from django.urls import path, include 
from . import views

urlpatterns=[
    
    path('', views.index , name='index'),
    path('all_emp', views.all_emp , name='view'),
    path('add_emp', views.add_emp , name='add'),
    path('remove_emp', views.remove_emp , name='remove'),
    path('remove_emp/<int:emp_id>', views.remove_emp , name='remove'),
   
]