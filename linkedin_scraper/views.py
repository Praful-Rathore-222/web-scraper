from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.core.paginator import Paginator

# for linkedin scraper
from configparser import ConfigParser
from selenium import webdriver
from .utilities import (login,
                        scroll_to_bottom,
                        get_profiles_link_and_scrap_profiles
                        )


class RefreshEmployeeList(APIView):
    """
    fetch employees from Linkedin, and upsert them.
    """
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        driver = webdriver.Chrome('linkedin_scraper/chromedriver_linux64/chromedriver')

        # Loading of configurations
        config = ConfigParser()
        config.read('config.ini')

        # Doing login on LinkedIn
        username = config.get('linkedin', 'username')
        password = config.get('linkedin', 'password')
        if username and password:
            login(driver, username, password)
            driver.get('https://www.linkedin.com/company/mambu/people/')
            scroll_to_bottom(driver=driver)
            get_profiles_link_and_scrap_profiles(driver)
        else:
            print('Enter the cridentials in the config file')

        driver.quit()

        return Response({'success': 'Profiles are successfully scraped.'}, status=status.HTTP_200_OK)


class EmployeeList(APIView):
    """
    List all mambu employees.
    """

    def get(self, request, format=None):
        employee_list = Employee.objects.all()
        page = request.GET.get('page')
        paginator = Paginator(employee_list, 10)
        employees = paginator.get_page(page)
        serializer = EmployeeSerializer(employees, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class EmployeeDetail(APIView):
    """
    Retrieve an Employee detail.
    """

    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        employee = self.get_object(pk=pk)
        serializer = EmployeeSerializer(employee, context={'request': request})
        return Response(serializer.data)
