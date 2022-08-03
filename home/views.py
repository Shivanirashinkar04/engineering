
import code
from secrets import choice
from urllib.request import Request
from django.shortcuts import render
from .models import Combine,Coursename,Programname,Courselevel,EngineeringColleges4May,Engineering28May, master_course,master_institute
from django.shortcuts import redirect
from .forms import EnggForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

from django.http import HttpResponse
from django.db import connection

import csv

cursor = connection.cursor()
# Create your views here.
def EnggIndia(request):
    region = Engineering28May.objects.values('regionname').distinct()
    district = Engineering28May.objects.values('districtname').distinct()
    taluka = Engineering28May.objects.values('talukaname').distinct()
    minority = Engineering28May.objects.values('institutestatusminority').distinct()
    status = Engineering28May.objects.values('institutestatus').distinct()
    courselevel = master_course.objects.values('institutecode','courselevelname').distinct()
    cl = Courselevel.objects.all()
    program = master_course.objects.values('institutecode','programname').distinct()
    p = Programname.objects.all()
    course = master_course.objects.values('institutecode','coursename').distinct()
    cns = Coursename.objects.all()
    engg = Engineering28May.objects.all()
    return render(request, 'home/viewColleges.html',{'district':district,'region':region,'engg':engg,'taluka':taluka,'minority':minority,'status':status, 'courselevel':courselevel,'program':program,'course':course,'cl':cl,'p':p,'cns':cns})


def engineering_colleges(request):
    # form = Coalform()
    if request.method == 'POST':
        form = EnggForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            instance.user = request.user
            instance.save()
            print("data is saved.")
            return redirect('/engineering_colleges')
    else:
        form = EnggForm()
        queryset = Engineering28May.objects.all()
    return render(request,"home/engineering_colleges.html",{'form': form,'t':queryset})

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def region(request):
    t=[]
    region = Engineering28May.objects.values('regionname').distinct()
    # district = Engineering28May.objects.values('districtname').distinct()
    # taluka = Engineering28May.objects.values('talukaname').distinct()
    if(request.method == 'POST'):
        t = request.POST["region"]
    district = Engineering28May.objects.filter(regionname=t).distinct('districtname')
    print(district)
    return render(request, 'home/viewColleges.html',{'region':region,'district':district,'t':t})

@csrf_exempt
def college(request):
    t=[]
    region = Engineering28May.objects.values('regionname').distinct()
    # district = Engineering28May.objects.values('districtname').distinct()
    # taluka = Engineering28May.objects.values('talukaname').distinct()
    if(request.method == 'POST'):
        t = request.POST["region"]
    district = Engineering28May.objects.filter(regionname=t).distinct('districtname')
    queryset = Engineering28May.objects.all().distinct()

    # print(queryset[0].institutecode.programname)
    # print(request.POST['region'])
    return render(request, 'home/viewColleges.html',{'region':region,'district':district,'t':queryset})

@csrf_exempt
def more(request):
    print(request.POST['data'])
    institutecode = (request.POST['data'])
    code = Engineering28May.objects.values('institutecode').filter(institutecode=institutecode).distinct()
    choice = master_course.objects.values('choicecode','coursename','coursedurationyear','programname','intakecurrentyear_aspergr').filter(institutecode=institutecode).distinct('coursename','programname','intakecurrentyear_aspergr','nbaaccreditation_status')
    NBA = master_course.objects.values('nbaaccreditation_status').filter(institutecode=institutecode).distinct()
    establishment = Engineering28May.objects.values('instituteestablishmentyear').filter(institutecode=institutecode).distinct()
    return render(request, 'home/management.html',{'code':code,'choice':choice,'establishment':establishment,'NBA':NBA})
