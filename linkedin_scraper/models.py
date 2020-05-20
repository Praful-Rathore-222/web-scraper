from django.db import models


class Employee(models.Model):
    company = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, null=True)
    designation = models.CharField(max_length=50)
    profile_photo_url = models.URLField(max_length=200, null=True, blank=True)
    employed_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.name} {self.designation}"

    class Meta:
        ordering = ['employed_date']
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
