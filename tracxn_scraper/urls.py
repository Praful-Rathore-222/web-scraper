from django.urls import path
from .views import CompanyDetail, CompanyList

app_name = 'tracxn_scraper'

urlpatterns = [
    path('api/v1/', CompanyList.as_view(), name='company-list'),
    path('api/v1/<int:pk>/', CompanyDetail.as_view(), name='company-detail'),
]
