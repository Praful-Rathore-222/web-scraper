from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Company, Category, Investor, NewsLink


def create_category(name='default category'):
    """
    Utility function to create category.
    :param name:
    :return:
    """
    category = Category.objects.create(name=name)
    return category


def create_investor(name='default investor', is_angel=False):
    """
    Utility function to create investor.
    :param name:
    :param is_angel:
    :return:
    """
    investor = Investor.objects.create(name=name, is_angel=True)
    return investor


def create_company(category,
                   name='default company',
                   short_description='default company created for test cases',
                   founded_year=2010,
                   location='default location'):
    """
    Utility function to create Company.
    :param name:
    :param short_description:
    :param founded_year:
    :param location:
    :param investor:
    :param category:
    :return:
    """
    company = Company(name=name,
                      short_description=short_description,
                      founded_year=founded_year,
                      location=location)
    company.save()
    company.category.add(category)
    return company


def create_newslink(company, title='default newslink for a company'):
    """
    Utility function to create newslink.
    :param title:
    :param company:
    :return:
    """
    newslink = NewsLink(title=title)
    newslink.save()
    newslink.company.set(company)
    return newslink


class CompanyListTest(APITestCase):

    def test_no_company(self):
        """
        If no company exists an empty list should be returned.
        """
        response = self.client.get(reverse('tracxn_scraper:company-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Company.objects.count(), 0)
        self.assertQuerysetEqual(response.data, [])

    def test_company_exists(self):
        """
        If company exists a company object should be returned.
        """
        category = create_category()
        company = create_company(category,
                                 name='test company name')
        response = self.client.get(reverse('tracxn_scraper:company-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Company.objects.count(), 1)
        self.assertContains(response, 'test company name')


class CompanyDetailTest(APITestCase):
    def test_no_company(self):
        """
        If company not exists status code 404 should return.
        """
        response = self.client.get(reverse('tracxn_scraper:company-detail', args=(2,)))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_company_exists(self):
        """
        If company exists a company object should be returned.
        """
        category = create_category()
        company = create_company(category,
                                 name='test company name')
        response = self.client.get(reverse('tracxn_scraper:company-detail', args=(company.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'test company name')
