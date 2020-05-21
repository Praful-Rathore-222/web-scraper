from django.contrib import admin
from .models import Category, Company, Investor, NewsLink


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'total_funding')


class InvestorAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_angel')


class NewsLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'company')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Investor, InvestorAdmin)
admin.site.register(NewsLink, NewsLinkAdmin)
