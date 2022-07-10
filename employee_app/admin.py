from django.contrib import admin
from employee_app.models import Employee, Position, Department

admin.site.register(Employee)
admin.site.register(Position)
admin.site.register(Department)
