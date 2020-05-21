from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Employee

AdminSite.site_header = 'Webscraper Admin'
AdminSite.index_title = 'Welcome to administrative area'


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'designation', 'employed_date')


admin.site.register(Employee, EmployeeAdmin)
