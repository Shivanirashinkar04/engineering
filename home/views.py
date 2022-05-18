from django.shortcuts import render
from .models import EngineeringColleges4May#, ProjectDetails,
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