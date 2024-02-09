from django.db import models

# Create your models here.
class Countries(models.Model):
    country_name = models.CharField(max_length=120)
    temp_cm = models.IntegerField()
    temp_fm = models.IntegerField()