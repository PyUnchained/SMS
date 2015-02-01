import os
import inspect
import importlib
from django.shortcuts import render
from django.apps import apps

from search_box.lookups import*

from sms.settings import BASE_DIR

from office.utility import add_to, remove_from
from gem_soft.utility import dynamic_import, find_modules

#Find all models modules and import them... no real reason to
#have it though
for item in find_modules('models'):
	dynamic_import(item)



# Create your views here.
def testing(request, action = None, obj = None, extra_obj = None):

	#Find all models modules and import them... no real reason to
	#have it though
	for item in find_modules('models'):
		dynamic_import(item)

	extra_obj = Student.objects.get(pk =20)
	obj = Class.objects.get(pk=20)
	action = 'remove'

	if action and obj and extra_obj != None:
		if action == 'add':
			result = add_to(obj, extra_obj)

		elif action == 'remove':
			result = remove_from(obj, extra_obj)

	student = Student.objects.get(pk=20)
	teacher = Staff.objects.get(pk=10)
	course = Course.objects.get(pk=12)
	

	return render(request,'testing.html',
		{'test':result,
		'student':student,
		'teacher':teacher})

def search_actions(request, action = None, obj = None, extra_obj = None):

	if request.method == "POST":

		result = request.POST

		# if action and obj and extra_obj != None:
		# 	if action == 'add':
		# 		result = add_to(obj, extra_obj)

		# 	elif action == 'remove':
		# 		result = remove_from(obj, extra_obj)


		return render(request,'testing.html',
			{'test':result})

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

	if 'add' in search_what:	#Determine the type of search-box
		search_type = 'add'		#actions requested.
	elif 'view' in search_what:
		search_type = 'view'

	if 'Staff' in search_what:

		names, ids = lookup_staff(criteria)
		url_name = None

		return render(request,'search_result.html',
			{'test':criteria,
			'name_list':names,
			'id_list':ids,
			'url_name':url_name,
			'search_type':search_type,
			'search_what':search_what})

	if 'Student' in search_what:

		names, ids = lookup_students(criteria)
		url_name = 'view_one_student'
		
		return render(request,'search_result.html',
			{'test':criteria,
			'name_list':names,
			'id_list':ids,
			'url_name':url_name,
			'search_type':search_type,
			'search_what':search_what})

	if 'Course' in search_what:

		names, ids = lookup_courses(criteria)
		url_name = 'course_details'

		return render(request,'search_result.html',
			{'test':criteria,
			'name_list':names,
			'id_list':ids,
			'url_name':url_name,
			'search_type':search_type,
			'search_what':search_what})

	if 'Subject' in search_what:

		names, ids = lookup_subjects(criteria)
		url_name = 'subject_details'

		return render(request,'search_result.html',
			{'test':criteria,
			'name_list':names,
			'id_list':ids,
			'url_name':url_name,
			'search_type':search_type,
			'search_what':search_what})




	return render(request,'search_result.html',
		{'test':search_what})
