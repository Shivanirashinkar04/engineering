
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
    # coal = ProjectDetails.objects.all()
    # enggdata=EngineeringColleges4May.objects.all()
    region = Engineering28May.objects.values('regionname').distinct()
    district = Engineering28May.objects.values('districtname').distinct()
    taluka = Engineering28May.objects.values('talukaname').distinct()
    minority = Engineering28May.objects.values('institutestatusminority').distinct()
    status = Engineering28May.objects.values('institutestatus').distinct()
    courselevel = master_course.objects.values('institutecode','courselevelname').distinct()
    # print(courselevel)
    program = master_course.objects.values('institutecode','programname').distinct()
    course = master_course.objects.values('institutecode','coursename').distinct()
    
    # combine= Combine.objects.values_list('institutecode','courselevelname','programname','coursename').distinct()
    # print(courselevel)
    # district = Engineering28May.objects.values('districtname').distinct()
    # taluka = Engineering28May.objects.values('talukaname').distinct()
    # print(colleges)
    # s = Engineering28May.objects.raw('select * from engineering_28may')
    # print(type(s))
    # print(cursor.fetchall())
    # return render(request, 'home/viewColleges.html',{'region':region,'district':district,'taluka':taluka})
    engg = Engineering28May.objects.all()
    # courselevelengg = Courselevel.objects.all()
    # programnameengg = Programname.objects.all()
    # coursenameengg = Coursename.objects.all()
    print(engg[0].institutewebaddress)
    return render(request, 'home/viewColleges.html',{'district':district,'region':region,'engg':engg,'taluka':taluka,'minority':minority,'status':status, 'courselevel':courselevel,'program':program,'course':course})


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
    queryset = Engineering28May.objects.all()

    # print(queryset[0].institutecode.programname)
    # print(request.POST['region'])
    return render(request, 'home/viewColleges.html',{'region':region,'district':district,'t':queryset})

