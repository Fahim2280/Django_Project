from django.db import models

# Create your models here.

class Person(models.Model):
    date = models.DateTimeField()
    trade_code = models.CharField(max_length=100)
    high = models.FloatField(max_length=100)
    low = models.FloatField(max_length=100)
    open = models.FloatField(max_length=100)
    close = models.FloatField(max_length=100)
    volume = models.FloatField(max_length=100)


