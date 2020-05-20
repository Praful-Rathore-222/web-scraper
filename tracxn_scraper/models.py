from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Investor(models.Model):
    name = models.CharField(max_length=100)
    is_angel = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Investor'
        verbose_name_plural = 'Investors'


class Company(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255)
    description = models.TextField(null=True)
    founded_year = models.IntegerField()
    location = models.CharField(max_length=100)
    total_funding = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    stage = models.CharField(max_length=100, null=True)
    investor = models.ManyToManyField(Investor)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['name']
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class NewsLink(models.Model):
    title = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'NewsLink'
        verbose_name_plural = 'NewsLinks'
