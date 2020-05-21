from .models import Company
from .serializers import CompanySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.core.paginator import Paginator


class CompanyList(APIView):
    """
    List all companies present in tracxn.
    """
    def get(self, request, format=None):
        company_list = Company.objects.all()
        page = request.GET.get('page')
        paginator = Paginator(company_list, 10)
        companies = paginator.get_page(page)
        serializer = CompanySerializer(companies, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CompanyDetail(APIView):
    """
    Retrieve an Employee detail.
    """

    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        company = self.get_object(pk=pk)
        serializer = CompanySerializer(company, context={'request': request})
        return Response(serializer.data)
