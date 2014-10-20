from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=250)
    website = models.CharField(blank=True,null=True, max_length=300)