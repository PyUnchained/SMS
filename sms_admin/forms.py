import time
from datetime import date, timedelta

from django import forms
from django.contrib.auth.models import User

from office.models import Student, Staff, Campus, Course, Class
from office.models import Subject, Result

class EditStudentProfileForm(forms.ModelForm):
	
	class Meta:
		model = Student
		fields = ('personid', 'middle_name',
			'sex', 'date_of_birth', 'national_id', 'pic',
			'billing_address_street', 'billing_address_city',
			'billing_address_country', 'homephone', 'preffered_cell',
			'secondary_cell', 'tertiary_cell', 'email2', 'skype')

class EditUserForm(forms.ModelForm):
	
	class Meta:
		model = User
		fields = ('first_name','last_name','email')
