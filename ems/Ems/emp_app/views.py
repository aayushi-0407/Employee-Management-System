from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q
# Create your views here.

def index(request):
    return render(request , 'index.html')

def all_emp(request):
    emps=Employee.objects.all()
    context={
        'Employees': emps
    }
    print(context)
    return render(request , 'view_emp.html' ,context)

def add_emp(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        phone=int(request.POST['phone'])
        dept=(request.POST['dept'])
        role=(request.POST['role'])
        newdept=Department(name=dept, location='remote')
        newrole=Role(name=role)
        newdept.save()
        newrole.save()

        newemp= Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept=newdept, role=newrole , hire_date= datetime.now())
        newemp.save()
        return HttpResponse('Employee Added Successfully')
    elif request.method=="GET":
        return render(request , 'add_emp.html')
    else:
        return HttpResponse("An Exception Occured")
def remove_emp(request , emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee removed successfully")
    
        except:
            return HttpResponse("Enter a valid Emp ID")
    emps=Employee.objects.all()
    context={
        'emps':emps
    }

    return render(request , 'remove_emp.html' ,context)

