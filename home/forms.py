from django.db.models import fields
from django.forms import ModelForm
from .models import EngineeringColleges4May

from django import forms
class EnggForm(forms.ModelForm):
    class Meta:

       model=EngineeringColleges4May
       fields='__all__'