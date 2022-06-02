from django.shortcuts import render
from .models import EngineeringColleges4May,Engineering28May#, ProjectDetails,
from django.shortcuts import redirect
from .forms import EnggForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import csv
# Create your views here.
def EnggIndia(request):
    # coal = ProjectDetails.objects.all()
    enggdata=EngineeringColleges4May.objects.all()
    print(enggdata)
    context = {'enggdata':enggdata}
    # context = {'wells': wells, 'mylist':mylist}
    return render(request, 'home/viewColleges.html', context )


def enggindia(request):
    # coal = ProjectDetails.objects.all()
    enggdata=Engineering28May.objects.all()
    print(enggdata)
    context = {'enggdata':enggdata}
    # context = {'wells': wells, 'mylist':mylist}
    return render(request, 'home/viewColleges.html', context )


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
    return render(request,"home/engineering_colleges.html",{'form': form})

def export(request,institutecode):
    s=Engineering28May.objects.get(institutecode=institutecode)
    print(s)
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['College name', 'Address', 'City', 'Postal Address','District','Management','Latitude','Longitude'])

    for project in Engineering28May.objects.filter(institutenameenglish=s).values_list('institutecode', 'institutenameenglish', 'field_instituteaddressenglish_field', 'institutepin','field_instituteestablishmentyear_field','field_regionname_field','districtname','field_talukaname_field'):
        writer.writerow(project)

    response['Content-Disposition'] = 'attachment; filename="project_info.csv"'

    return response
        