import time
from datetime import date, timedelta

from django import forms
from django.contrib.auth.models import *

from office.models import*

class ClassSearchForm(forms.Form):
	new_classes = forms.CharField(max_length=300, widget=forms.TextInput(
		attrs={'id':'id_new_classes'}))