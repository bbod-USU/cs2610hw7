from django.db import models

# Create your models here.

class Converter(models.Model):
    units = models.CharField(max_length=200)
    value = models.FloatField()

def __str__(self):
    return '%s, %f' % (self.units, self.value)