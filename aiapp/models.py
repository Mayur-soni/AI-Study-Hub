from django.db import models

# Create your models here.
class Signup(models.Model):
    NAME=models.CharField(max_length=30)
    EMAIL=models.EmailField()
    PAS = models.CharField(max_length=30)

    def __str__(self):
        return self.NAME