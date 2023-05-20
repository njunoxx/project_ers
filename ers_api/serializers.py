from rest_framework import serializers
from app_employeewebsite.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("full_name", "contact", "email", "dob", "gender", "join_date", "address", "blood_group", "department", "user" )
