import time
from datetime import date, timedelta

from django import forms
from django.contrib.auth.models import *

from office.models import*

class ClassSearchForm(forms.Form):
	new_classes = forms.CharField(max_length=300, widget=forms.TextInput(
		attrs={'id':'id_new_classes'}))


class EditClassForm(forms.ModelForm):

	def __init__(self,*args,**kwargs):

		#Remove pk key from kwargs dictionary before initializing the
		#class to prevent errors.
		if kwargs.has_key('pk'):
			pk = kwargs['pk']
			kwargs.pop('pk',None)

		super (EditClassForm,self ).__init__(*args,**kwargs) #populates form

		#Change the queryset used to only show the students and
		#teachers currently part of the class
		if kwargs.has_key('instance'):
			target_class = kwargs['instance']
		else:
			target_class = Class.objects.get(pk = pk)
		self.fields['teachers'].queryset = target_class.teachers.all()



	class Meta:
		model = Class
		fields = ('code', 'teachers', 'course', 'exam_date',
			'min_students', 'max_students', 'schedule')


class EditCourseForm(forms.ModelForm):

	class Meta:
		model = Course
		fields = ('title', 'subtitle', 'syllabus_code', 'campuses',
			'price', 'duration', 'info_file')

class EditSubjectForm(forms.ModelForm):
	
	class Meta:
		model = Subject
		exclude = ('is_active',)
		
