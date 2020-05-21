from django.urls import path
from .views import EmployeeDetail, EmployeeList, RefreshEmployeeList

app_name = 'linkedin_scraper'

urlpatterns = [
    path('api/v1/', EmployeeList.as_view(), name='employee-list'),
    path('api/v1/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),
    path('api/v1/refresh/', RefreshEmployeeList.as_view(), name='refresh-linkedin-employees')
]

