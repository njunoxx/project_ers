from django.urls import path, include
from .import views
urlpatterns = [
path('employee/', views.employee_index, name='emp-index'),
path('employee/show/<int:id>/', views.employee_show, name='emp-show'),
path('employee/edit/<int:id>/', views.employee_edit, name='emp-edit'),
path('employee/delete/<int:id>/', views.employee_delete, name='emp-delete'),
path('employee/add/', views.employee_add, name='emp-add'),
path('employee/update/', views.employee_update, name='emp-update'),
path('department/', views.department_index, name='dep-index'),
path('department/show/<int:id>/', views.department_show, name='dep-show'),
path('department/add/', views.department_add, name='dep-add'),
path('department/edit/<int:id>', views.department_edit, name='dep-edit'),
path('department/update/', views.department_update, name='dep-update'),
path('department/delete/<int:id>/', views.department_delete , name='dep-delete'),
path('salary/', views.salary_index, name='sal-index'),
path('salary/show/<int:id>/', views.salary_show, name='sal-show'),
path('salary/add/', views.salary_add, name='sal-add' ),
path('salary/edit/<int:id>', views.salary_edit, name='sal-edit'),
path('salary/update/', views.salary_update, name='sal-update'),
path('salary/delete/<int:id>/', views.salary_delete, name='sal-delete'),


]