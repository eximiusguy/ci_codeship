from django.forms import ModelForm
from employee.models import Employee
from django.core.validators import validate_email


class RegistrationForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name','email','website']