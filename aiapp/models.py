from django.db import models


class Signup(models.Model):
    NAME = models.CharField(max_length=100)
    EMAIL = models.EmailField(unique=True)
    PAS = models.CharField(max_length=128)
    ROLE = models.CharField(max_length=50, default='student')

    def __str__(self):
        return self.EMAIL

class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.JSONField()  # List of strings
    application_link = models.URLField()


