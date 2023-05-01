from django.db import models

# Create your models here.
class Notes(models.Model):
    notes = models.TextField()

class Profile(models.Model):
    name = models.CharField()
    zipcode = models.CharField()