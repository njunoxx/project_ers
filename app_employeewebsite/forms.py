from django import forms
from .models import Employee
from .models import Department
from .models import EmployeeSalary
class EmployeeCreateForm(forms.ModelForm):
    """ Form CLass for Employee Creation"""
    class Meta:
        fields = "__all__"
        #fields = ("fullname","contact")
        model = Employee

class DepartmentCreateForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = Department

class SalaryCreateForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = EmployeeSalary