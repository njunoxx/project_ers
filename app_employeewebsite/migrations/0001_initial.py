# Generated by Django 4.1.6 on 2023-02-15 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=255)),
                ('short_name', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'app_department',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('join_date', models.DateField()),
                ('gender', models.CharField(max_length=255)),
                ('blood_group', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_employeewebsite.department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'app_employee',
            },
        ),
        migrations.CreateModel(
            name='EmployeeSalary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary_amount', models.FloatField()),
                ('bonus_amount', models.FloatField(default=0)),
                ('allowance', models.FloatField(default=0)),
                ('tds_in_percent_amount', models.FloatField(default=1)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.BooleanField(default=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_employeewebsite.employee')),
            ],
            options={
                'db_table': 'app_employee_salary',
            },
        ),
        migrations.CreateModel(
            name='EmployeeAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('attend_date', models.DateField()),
                ('check_in_time', models.CharField(max_length=255)),
                ('check_out_time', models.CharField(max_length=255)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_employeewebsite.employee')),
            ],
            options={
                'db_table': 'app_employee_attendance',
            },
        ),
    ]
