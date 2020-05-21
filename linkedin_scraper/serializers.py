from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='linkedin_scraper:employee-detail', read_only=True)

    class Meta:
        model = Employee
        fields = ['url', 'id', 'company', 'name', 'email', 'designation', 'profile_photo_url', 'employed_date']

