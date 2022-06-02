# from django.db import models
from django.contrib.gis.db import models
from django.db.models.fields.files import ImageField
from PIL import Image
import sys
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import datetime


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


class Engineering28May(models.Model):
    geom = models.GeometryField(blank=True, null=True)
    institutecode = models.IntegerField(blank=True, null=True)
    institutenameenglish = models.CharField(max_length=255, blank=True, null=True)
    field_instituteaddressenglish_field = models.CharField(db_column="'InstituteAddressEnglish'", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    institutepin = models.IntegerField(blank=True, null=True)
    field_instituteestablishmentyear_field = models.IntegerField(db_column="'InstituteEstablishmentYear'", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_regionname_field = models.CharField(db_column="'RegionName'", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    districtname = models.CharField(max_length=255, blank=True, null=True)
    field_talukaname_field = models.CharField(db_column="'TalukaName'", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_institutewebaddress_field = models.CharField(db_column="'InstituteWebAddress'", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_instituteemailid_field = models.CharField(db_column="'InstituteEmailID'", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_institutestdcode_field = models.CharField(db_column="'InstituteSTDCode'", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_boyshostelcapacitytotal_field = models.IntegerField(db_column="'BoysHostelCapacityTotal'", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_girlshostelcapacitytotal_field = models.IntegerField(db_column="'GirlsHostelCapacityTotal'", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_principalnameenglish_field = models.CharField(db_column="'PrincipalNameEnglish'", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_principalofficephoneno_field = models.CharField(db_column="'PrincipalOfficePhoneNo'", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_institutestatus_field = models.CharField(db_column="'InstituteStatus'", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_institutestatusautonomy_field = models.CharField(db_column="'InstituteStatusAutonomy'", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_institutestatusminority_field = models.CharField(db_column="'InstituteStatusMinority'", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_naacstatus_field = models.CharField(db_column="'NAACStatus'", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_lettergrade_field = models.CharField(db_column="'LetterGrade'", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_longitude_field = models.FloatField(db_column="'Longitude'", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_latitude_field = models.FloatField(db_column="'Latitude'", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    picture = models.ImageField(upload_to='EngineeringPics/', blank=True, null=True, default='')
    class Meta:
        managed = False
        db_table = 'engineering_28may'


class MasterCourse(models.Model):
    institutecode = models.CharField(max_length=200, blank=True, null=True)
    choicecode = models.CharField(max_length=200, blank=True, null=True)
    courselevelname = models.CharField(max_length=200, blank=True, null=True)
    programname = models.CharField(max_length=200, blank=True, null=True)
    coursename = models.CharField(max_length=200, blank=True, null=True)
    universityname = models.CharField(max_length=200, blank=True, null=True)
    coursestartyear = models.CharField(max_length=200, blank=True, null=True)
    coursedurationyear = models.CharField(max_length=200, blank=True, null=True)
    nbaaccreditation_status = models.CharField(max_length=200, blank=True, null=True)
    accreditation_from = models.CharField(max_length=200, blank=True, null=True)
    accreditation_to = models.CharField(max_length=200, blank=True, null=True)
    intakecurrentyear_aspergr = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_course'

class MasterInstitute(models.Model):
    institutecode = models.DecimalField(max_digits=50, decimal_places=0, blank=True, null=True)
    institutename = models.CharField(max_length=300, blank=True, null=True)
    instituteaddress = models.CharField(max_length=300, blank=True, null=True)
    institutepin = models.DecimalField(max_digits=50, decimal_places=0, blank=True, null=True)
    establish_year = models.CharField(max_length=50, blank=True, null=True)
    regionname = models.CharField(max_length=50, blank=True, null=True)
    districtname = models.CharField(max_length=50, blank=True, null=True)
    talukaname = models.CharField(max_length=50, blank=True, null=True)
    institutewebaddress = models.CharField(max_length=200, blank=True, null=True)
    institutestdcode = models.CharField(max_length=50, blank=True, null=True)
    boyshostelcapacitytotal = models.CharField(max_length=50, blank=True, null=True)
    girlshostelcapacitytotal = models.CharField(max_length=50, blank=True, null=True)
    principalname = models.CharField(max_length=200, blank=True, null=True)
    principalofficephoneno = models.CharField(max_length=20, blank=True, null=True)
    institutestatus = models.CharField(max_length=50, blank=True, null=True)
    institutestatusautonomy = models.CharField(max_length=50, blank=True, null=True)
    institutestatusminority = models.CharField(max_length=200, blank=True, null=True)
    naacstatus = models.CharField(max_length=50, blank=True, null=True)
    lettergrade = models.CharField(max_length=50, blank=True, null=True)
    instituteemailid = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_institute'        