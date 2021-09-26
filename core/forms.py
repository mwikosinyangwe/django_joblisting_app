from django import forms
from django.forms import ModelForm, TextInput
from .models import *


class CreateJobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = "__all__"
        