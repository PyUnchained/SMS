import os
import inspect
import importlib
from django.shortcuts import render
from django.apps import apps

from search_box.lookups import*

from sms.settings import BASE_DIR

from bookkeep.models import*
from office.models import*
from cal.models import*
from msg_box.models import*
from sms_admin.models import*
from office.utility import add_to


# Create your views here.
def testing(request, action = None, obj = None, extra_obj = None):

	extra_obj = Subject.objects.get(pk =10)
	obj = Class.objects.get(pk=20)
	action = 'add'

	if action and obj and extra_obj != None:
		if action == 'add':
			result = add_to(obj, extra_obj)

	student = Student.objects.get(pk=20)
	teacher = Staff.objects.get(pk=10)
	course = Course.objects.get(pk=12)

	return render(request,'testing.html',
		{'test':result,
		'student':student,
		'teacher':teacher,
		'course':course})

def search(request):

	question = request.GET.get('q')

	#
	current_index = 0
	for char in question:
		if char == ']':
			search_what = question[:current_index+1]
			question = question[current_index+2:]
			break
		else:
			current_index +=1

	criteria = question.split('-')
	if 'view' in search_what:
		if 'staff' in search_what:

			names, ids = lookup_staff(criteria)

			return render(request,'search_result.html',
				{'test':criteria,
				'name_list':names,
				'id_list':ids,
				'list_variant':'staff'})

		if 'students' in search_what:

			names, ids = lookup_students(criteria)

			return render(request,'search_result.html',
				{'test':criteria,
				'name_list':names,
				'id_list':ids,
				'list_variant':'students'})

		if 'courses' in search_what:

			names, ids = lookup_courses(criteria)

			return render(request,'search_result.html',
				{'test':criteria,
				'name_list':names,
				'id_list':ids,
				'list_variant':'courses'})

		if 'subjects' in search_what:

			names, ids = lookup_subjects(criteria)

			return render(request,'search_result.html',
				{'test':criteria,
				'name_list':names,
				'id_list':ids,
				'list_variant':'courses'})



	return render(request,'search_result.html',
		{'test':search_what})
