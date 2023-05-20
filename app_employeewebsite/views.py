from django.shortcuts import render, redirect
from .forms import EmployeeCreateForm,  DepartmentCreateForm, SalaryCreateForm
from .models import Employee, User, Department, EmployeeSalary
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def employee_index(request):
    """ Returns list of employee as context"""
    employee_list = Employee.objects.all()
    context= {"data": employee_list}

    if request.method == "POST":
        dataList = Employee.objects.filter(full_name=request.POST.get('full_name'))
        context.update({"data":dataList})
        return render(request, 'employees/index_employee.html', context)
    
    
    return render(request, 'employees/index_employee.html',context)

def employee_add(request):
    emp_create_form = EmployeeCreateForm()
    context = {"form": emp_create_form}

    if request.method == "POST":
        emp = Employee()
        user = User.objects.get(id=request.POST.get('user'))
        department = Department.objects.get(id=request.POST.get('department'))
        emp.full_name = request.POST.get('full_name')
        emp.address = request.POST['address']
        emp.blood_group = request.POST.get('blood_group')
        emp.contact = request.POST.get('contact')
        emp.email = request.POST.get('email')
        emp.dob = request.POST.get('dob')
        emp.gender = request.POST.get('gender')
        emp.join_date = request.POST.get('join_date')
        emp.user = user
        emp.department = department
        emp.save()

        messages.success(request, 'Employee added successfully')

        return redirect('emp-index')
    return render(request, 'employees/add_employee.html', context)

def employee_update(request):
    if request.method == "POST":
        user =User.objects.get(id=request.POST.get('user'))
        department = Department.objects.get(id=request.POST.get('department'))
        emp = Employee.objects.get(id=request.POST.get('id'))
        emp.full_name = request.POST.get('full_name')
        emp.email = request.POST.get('email')
        emp.address = request.POST.get('address')
        emp.blood_group = request.POST.get('blood_group')
        emp.contact = request.POST.get('contact')
        emp.email = request.POST.get('email')
        emp.dob = request.POST.get('dob')
        emp.gender = request.POST.get('gender')
        emp.join_date = request.POST.get('join_date')
        emp.user = user
        emp.department = department
        emp.save()
    return redirect("emp-index")

def employee_edit(request, id):
    data = Employee.objects.get(id=id)
    department= Department.objects.all()
    user= User.objects.all()
    
    context = {"data": data, "department": department, "user": user}
    return render(request, 'employees/edit_employee.html',context)

def employee_show(request, id):
      data = Employee.objects.get(id=id)
      data1 = Employee.objects.all()
      context = {"data": data, "data1":data1}
      return render(request, 'employees/show_employee.html', context)

def employee_delete(request, id):
    data = Employee.objects.get(id=id)
    data.delete()
    return redirect("emp-index")

def department_index(request):
    dep_data = Department.objects.all()
    context = {"data": dep_data}
    return render(request, 'departments/index_department.html',context)

def department_show(request, id):
    dep_data = Department.objects.get(id=id)
    context = {"data": dep_data}
    return render(request, 'departments/show_department.html', context)

def department_edit(request, id):
    dep_data = Department.objects.get(id=id)
    context = {"data": dep_data}

    return render(request, 'departments/edit_department.html', context)


def department_update(request):
    if request.method == "POST":
        dep = Department.objects.get(id=request.POST.get('id'))
        dep.department_name = request.POST.get('department_name')
        dep.short_name = request.POST.get('short_name')
        dep.status = True if request.POST.get("status") =="status" else False
        dep.save()
        return redirect('dep-index')    



def department_delete(request, id):
    dep_data = Department.objects.get(id=id)
    dep_data.delete()
    messages.success(request, 'Department deleted successfully.')
    return redirect('dep-index')

def department_add(request):
    dep_create_form = DepartmentCreateForm()
    context = {"form": dep_create_form}
    
    if request.method == "POST":
        dep = Department()
        dep.department_name = request.POST.get('department_name')
        dep.short_name = request.POST.get('short_name')
        dep.status = True if request.POST.get("status") == "on" else False
        dep.save()
        
        messages.success(request, 'Department added successfully')
        
        return redirect('dep-index')

    return render(request, 'departments/add_department.html',context)

def salary_index(request):
    sal_data = EmployeeSalary.objects.all()
    context = {"data": sal_data}
    return render(request, 'salaryrecords/index_salary_record.html', context)

def salary_edit(request, id):
    sal_data = EmployeeSalary.objects.get(id=id)
    context = {"data": sal_data}
    
    return render(request, 'salaryrecords/edit_salary_record.html', context)

def salary_update(request):
    if request.method == "POST":
        sal = EmployeeSalary.objects.get(id=request.POST.get('id'))
        sal.salary_amount = request.POST.get('salary_amount')
        sal.bonus_amount = request.POST.get('bonus_amount')
        sal.allowance = request.POST.get('allowance')
        sal.tds_in_percent_amount = request.POST.get('tds_in_percent_amount')
        sal.start_date = request.POST.get('start_date')
        sal.end_date = request.POST.get('end_date')
        sal.save()

        messages.success(request, 'Department added successfully')

        return redirect('sal-index')

def salary_show(request, id):
    sal_data = EmployeeSalary.objects.get(id=id)
    context = {"data": sal_data}
    return render(request, 'salaryrecords/show_salary_record.html', context)

def salary_add(request):
    sal_create_form = SalaryCreateForm()
    context = {"form":sal_create_form}

    if request.method == "POST":
        sal = EmployeeSalary()
        employee = Employee.objects.get(id=request.POST.get('employee'))
        sal.salary_amount = request.POST.get('salary_amount')
        sal.bonus_amount = request.POST.get('bonus_amount')
        sal.allowance = request.POST.get('allowance')
        sal.tds_in_percent_amount = request.POST.get('tds_in_percent_amount')
        sal.start_date = request.POST.get('start_date')
        sal.end_date = request.POST.get('end_date')
        sal.employee = employee 
        sal.save()

        messages.success(request, 'Salary of employee added successfully')
        return redirect('sal-index')

    return render(request, 'salaryrecords/add_salary_record.html', context)

def salary_delete(request, id):
    sal_data = EmployeeSalary.objects.get(id=id)
    sal_data.delete()

    messages.success(request, 'Salary of employee deleted successfully')
    return redirect('sal-index')

def master(request):
    return render(request, 'layouts/master.html')

