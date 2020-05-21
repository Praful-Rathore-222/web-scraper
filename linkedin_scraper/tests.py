from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Employee


def create_employee(company='mambu', name='test_name', designation='test_des'):
    """
    Utility function to create employee record.
    :param company:
    :param name:
    :param designation:
    :return:
    """
    employee = Employee.objects.create(company=company, name=name, designation=designation)
    return employee


class EmployeeListTest(APITestCase):

    def test_no_employees(self):
        """
        If no employee exists an empty list should be returned.
        """
        response = self.client.get(reverse('linkedin_scraper:employee-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Employee.objects.count(), 0)
        self.assertQuerysetEqual(response.data, [])

    def test_employee_exists(self):
        """
        If employee exists an employee object should be returned.
        """
        employee = create_employee(name='test employee name', designation='test designation')
        response = self.client.get(reverse('linkedin_scraper:employee-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Employee.objects.count(), 1)
        self.assertContains(response, 'test employee name')


class EmployeeDetailTest(APITestCase):
    def test_no_employee(self):
        """
        If employee not exists status code 404 should return.
        """
        response = self.client.get(reverse('linkedin_scraper:employee-detail', args=(2,)))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_employee_exists(self):
        """
        If employee exists an employee object should be returned.
        """
        employee = create_employee(name='test employee name', designation='test designation')
        response = self.client.get(reverse('linkedin_scraper:employee-detail', args=(employee.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'test employee name')
