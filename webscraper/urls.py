from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('linkedin_scraper/', include('linkedin_scraper.urls')),
    path('tracxn_scraper/', include('tracxn_scraper.urls')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
