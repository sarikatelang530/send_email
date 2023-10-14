from django.contrib import admin
from .models import Employee
# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','birthday', 'work_anniversary','email']

admin.site.register(Employee,EmployeeAdmin)


