from django.db import models

class CompensationData(models.Model):
    Timestamp = models.DateField(null=True)
    Age = models.IntegerField(null=True)
    Industry = models.CharField(max_length=255, null=True)
    JobTitle = models.CharField(max_length=255, null=True)
    Salary = models.FloatField(null=True)
    Currency = models.CharField(max_length=50, null=True)
    Location = models.CharField(max_length=255, null=True)
    Experience = models.IntegerField(null=True)
    Additional_information = models.TextField(null=True)
    Other = models.CharField(max_length=255, null=True)