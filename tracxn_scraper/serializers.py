from rest_framework import serializers
from .models import Category, Investor, Company, NewsLink


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = ['id', 'name', 'is_angel']


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='tracxn_scraper:company-detail', read_only=True)
    investor = InvestorSerializer(many=True)
    category = CategorySerializer(many=True)

    class Meta:
        model = Company
        fields = ['url',
                  'id',
                  'name',
                  'short_description',
                  'description',
                  'founded_year',
                  'location',
                  'total_funding',
                  'stage',
                  'investor',
                  'category']


class NewsLinkSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = NewsLink
        fields = ['id', 'name', 'company']
