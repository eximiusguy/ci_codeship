from django.shortcuts import render
from employee.forms import RegistrationForm
from employee.models import Employee
from django.contrib import messages
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect


def employee_registration(request):
    """Shows employee registration form. Employees can be registered from this view."""
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee data saved successfully.")
            return HttpResponseRedirect("/employee-list")
    else:
        form = RegistrationForm()
    c.update({'form':form})
    return render(request, "register.html", c)


def employee_listing(request):
    emp = Employee.objects.all()
    return render(request, "employee-list.html", {'employee_list':emp})