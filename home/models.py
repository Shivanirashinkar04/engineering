# from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class EngineeringColleges4May(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    geom = models.GeometryField(blank=True, null=True)
    field_1 = models.BigIntegerField(blank=True, null=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    city = models.CharField(max_length=254, blank=True, null=True)
    postaladdr = models.CharField(max_length=254, blank=True, null=True)
    district = models.CharField(max_length=254, blank=True, null=True)
    management = models.CharField(max_length=254, blank=True, null=True)
    yesno1 = models.CharField(max_length=254, blank=True, null=True)
    yesno2 = models.CharField(max_length=254, blank=True, null=True)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engineering_colleges_4may'