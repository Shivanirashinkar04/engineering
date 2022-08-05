# from django.db import models
from pyexpat import model
from django.contrib.gis.db import models
from sqlalchemy import true

# Create your models here.
class Engineering28May(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    geom = models.GeometryField(blank=True, null=True)
    institutecode = models.BigIntegerField(unique=True,blank=True, null=True)
    institutenameenglish = models.CharField(max_length=254, blank=True, null=True)
    instituteaddressenglish = models.CharField(max_length=254, blank=True, null=True)
    regionname = models.CharField(max_length=254, blank=True, null=True)
    districtname = models.CharField(max_length=254, blank=True, null=True)
    talukaname = models.CharField(max_length=254, blank=True, null=True)
    instituteemailid = models.CharField(max_length=254, blank=True, null=True)
    institutestdcode = models.CharField(max_length=254, blank=True, null=True)
    boyshostelcapacitytotal = models.BigIntegerField(blank=True, null=True)
    girlshostelcapacitytotal = models.BigIntegerField(blank=True, null=True)
    instituteestablishmentyear =models.CharField(max_length=254,blank=True,null=True)
    institutepin = models.CharField(max_length=254,blank=True,null=True)
    principalnameenglish = models.CharField(max_length=254, blank=True, null=True)
    principalofficephoneno = models.CharField(max_length=254, blank=True, null=True)
    institutestatus = models.CharField(max_length=254, blank=True, null=True)
    institutestatusautonomy = models.CharField(max_length=254, blank=True, null=True)
    institutestatusminority = models.CharField(max_length=254, blank=True, null=True)
    naccstatus = models.CharField(max_length=254, blank=True, null=True)
    lettergrade = models.CharField(max_length=254, blank=True, null=True)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    institutewebaddress = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'engineering_28may'

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


#create your models here
class master_course(models.Model):
    id=models.AutoField(primary_key=True)
    # institutecode=models.ForeignKey(Engineering28May,on_delete=models.SET_NULL, null=True,default=0,blank=True)
    institutecode=models.BigIntegerField()
    choicecode=models.CharField(max_length=254,blank=True, null=True)
    courselevelname=models.CharField(max_length=254,blank=True, null=True)
    programname=models.CharField(max_length=254, blank=True, null=True)
    coursename=models.CharField(max_length=254, blank=True, null=True)
    universityname=models.CharField(max_length=254, blank=True, null=True)
    coursestartyear=models.CharField(max_length=254, blank=True, null=True)
    coursedurationyear=models.CharField(max_length=254, blank=True, null=True)
    nbaaccreditation_status=models.CharField(max_length=254, blank=True, null=True)
    accreditation_from=models.CharField(max_length=254, blank=True, null=True)
    accreditation_to=models.CharField(max_length=254, blank=True, null=True)
    intakecurrentyear_aspergr=models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_course'


#create your models here
class master_institute(models.Model):
    institutecode=models.CharField(primary_key=True, max_length=20)
    institutename=models.CharField(max_length=254,blank=True, null=True)
    instituteaddress=models.CharField(max_length=254,blank=True, null=True)
    institutepin=models.CharField(max_length=254, blank=True, null=True)
    establish_year=models.CharField(max_length=254, blank=True, null=True)
    regionname=models.CharField(max_length=254, blank=True, null=True)
    districtname=models.CharField(max_length=254, blank=True, null=True)
    talukaname=models.CharField(max_length=254, blank=True, null=True)
    institutewebaddress=models.CharField(max_length=254, blank=True, null=True)
    institutestdcode=models.CharField(max_length=254, blank=True, null=True)
    boyshostelcapacitytotal=models.CharField(max_length=254, blank=True, null=True)
    principalname=models.CharField(max_length=254, blank=True, null=True)
    principalofficephoneno=models.CharField(max_length=254, blank=True, null=True)
    institutestatus=models.CharField(max_length=254, blank=True, null=True)
    institutestatusautonomy=models.CharField(max_length=254, blank=True, null=True)
    institutestatusminority=models.CharField(max_length=254, blank=True, null=True)
    naacstatus=models.CharField(max_length=254, blank=True, null=True)
    lettergrade=models.CharField(max_length=254, blank=True, null=True)
    instituteemailid=models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_institute'
  
class Combine(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    geom = models.GeometryField(blank=True, null=True)
    institutecode = models.BigIntegerField(unique=True,blank=True, null=True)
    institutenameenglish = models.CharField(max_length=254, blank=True, null=True)
    instituteaddressenglish = models.CharField(max_length=254, blank=True, null=True)
    regionname = models.CharField(max_length=254, blank=True, null=True)
    districtname = models.CharField(max_length=254, blank=True, null=True)
    talukaname = models.CharField(max_length=254, blank=True, null=True)
    instituteemailid = models.CharField(max_length=254, blank=True, null=True)
    institutestdcode = models.CharField(max_length=254, blank=True, null=True)
    boyshostelcapacitytotal = models.BigIntegerField(blank=True, null=True)
    girlshostelcapacitytotal = models.BigIntegerField(blank=True, null=True)
    principalnameenglish = models.CharField(max_length=254, blank=True, null=True)
    principalofficephoneno = models.CharField(max_length=254, blank=True, null=True)
    institutestatus = models.CharField(max_length=254, blank=True, null=True)
    institutestatusautonomy = models.CharField(max_length=254, blank=True, null=True)
    institutestatusminority = models.CharField(max_length=254, blank=True, null=True)
    naccstatus = models.CharField(max_length=254, blank=True, null=True)
    lettergrade = models.CharField(max_length=254, blank=True, null=True)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    coursename=models.CharField(max_length=254, blank=True, null=True)
    programname=models.CharField(max_length=254, blank=True, null=True)
    courselevelname=models.CharField(max_length=254,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'combine'

# Create your models here.
class Courselevel(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    geom = models.GeometryField(blank=True, null=True)
    institutecode = models.BigIntegerField(unique=True,blank=True, null=True)
    institutenameenglish = models.CharField(max_length=254, blank=True, null=True)
    instituteaddressenglish = models.CharField(max_length=254, blank=True, null=True)
    regionname = models.CharField(max_length=254, blank=True, null=True)
    districtname = models.CharField(max_length=254, blank=True, null=True)
    talukaname = models.CharField(max_length=254, blank=True, null=True)
    instituteemailid = models.CharField(max_length=254, blank=True, null=True)
    institutestdcode = models.CharField(max_length=254, blank=True, null=True)
    boyshostelcapacitytotal = models.BigIntegerField(blank=True, null=True)
    girlshostelcapacitytotal = models.BigIntegerField(blank=True, null=True)
    principalnameenglish = models.CharField(max_length=254, blank=True, null=True)
    principalofficephoneno = models.CharField(max_length=254, blank=True, null=True)
    institutestatus = models.CharField(max_length=254, blank=True, null=True)
    institutestatusautonomy = models.CharField(max_length=254, blank=True, null=True)
    institutestatusminority = models.CharField(max_length=254, blank=True, null=True)
    naccstatus = models.CharField(max_length=254, blank=True, null=True)
    lettergrade = models.CharField(max_length=254, blank=True, null=True)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    institutewebaddress = models.CharField(max_length=254)
    courselevelname = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'courselevel'

  
# Create your models here.
class Programname(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    geom = models.GeometryField(blank=True, null=True)
    institutecode = models.BigIntegerField(unique=True,blank=True, null=True)
    institutenameenglish = models.CharField(max_length=254, blank=True, null=True)
    instituteaddressenglish = models.CharField(max_length=254, blank=True, null=True)
    regionname = models.CharField(max_length=254, blank=True, null=True)
    districtname = models.CharField(max_length=254, blank=True, null=True)
    talukaname = models.CharField(max_length=254, blank=True, null=True)
    instituteemailid = models.CharField(max_length=254, blank=True, null=True)
    institutestdcode = models.CharField(max_length=254, blank=True, null=True)
    boyshostelcapacitytotal = models.BigIntegerField(blank=True, null=True)
    girlshostelcapacitytotal = models.BigIntegerField(blank=True, null=True)
    principalnameenglish = models.CharField(max_length=254, blank=True, null=True)
    principalofficephoneno = models.CharField(max_length=254, blank=True, null=True)
    institutestatus = models.CharField(max_length=254, blank=True, null=True)
    institutestatusautonomy = models.CharField(max_length=254, blank=True, null=True)
    institutestatusminority = models.CharField(max_length=254, blank=True, null=True)
    naccstatus = models.CharField(max_length=254, blank=True, null=True)
    lettergrade = models.CharField(max_length=254, blank=True, null=True)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    institutewebaddress = models.CharField(max_length=254)
   
    programname=models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'programname'

  
# Create your models here.
class Coursename(models.Model):
    coursename=models.CharField(max_length=254)
    id = models.CharField(primary_key=True, max_length=20)
    geom = models.GeometryField(blank=True, null=True)
    institutecode = models.BigIntegerField(unique=True,blank=True, null=True)
    institutenameenglish = models.CharField(max_length=254, blank=True, null=True)
    instituteaddressenglish = models.CharField(max_length=254, blank=True, null=True)
    regionname = models.CharField(max_length=254, blank=True, null=True)
    districtname = models.CharField(max_length=254, blank=True, null=True)
    talukaname = models.CharField(max_length=254, blank=True, null=True)
    instituteemailid = models.CharField(max_length=254, blank=True, null=True)
    institutestdcode = models.CharField(max_length=254, blank=True, null=True)
    boyshostelcapacitytotal = models.BigIntegerField(blank=True, null=True)
    girlshostelcapacitytotal = models.BigIntegerField(blank=True, null=True)
    principalnameenglish = models.CharField(max_length=254, blank=True, null=True)
    principalofficephoneno = models.CharField(max_length=254, blank=True, null=True)
    institutestatus = models.CharField(max_length=254, blank=True, null=True)
    institutestatusautonomy = models.CharField(max_length=254, blank=True, null=True)
    institutestatusminority = models.CharField(max_length=254, blank=True, null=True)
    naccstatus = models.CharField(max_length=254, blank=True, null=True)
    lettergrade = models.CharField(max_length=254, blank=True, null=True)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    institutewebaddress = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'coursename'
