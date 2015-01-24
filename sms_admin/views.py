import time
import json

from django.shortcuts import render, render_to_response, loader, redirect
from django.template import Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models import Q

#Required to safely format and return html
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from msg_box.models import Message
from office.models import *
from office.forms import *
from sms_admin.models import *
from sms_admin.forms import EditStudentProfileForm, EditUserForm


from sms_admin.conf import*
# Create your views here.

def reverse_trail_gen(trail = None):
	"""

	Produces HTML to use in an ordered breadcrumb. Takes one argument: trail.
	The trail is a list of tuples, each representing a breadcrumb.
	
	([order],[url-name],[breadcrumb-name])

	It is returned as an HTML string with breadcrumbs in order from 0 upwards.

	"""

	if trail != None:
		final_trail = ''
		trail_length = len(trail)


		for i in range (0,trail_length):
			for crumb in trail:

				#Find the crumb that's next in the order
				if crumb[0] == i:

					#Reverse the url and create an HTML string, including
					#the desired name of the breadcrumb link (crumb[2]).
					url = reverse(crumb[1])
					parts = ["> <a href = '" , url, "' > ", crumb[2], '</a>']
					parts = ''.join(parts)

					#Add this crumb to the rest of the crumbs
					final_trail = final_trail + parts

		#Return the full crumb html string.
		return final_trail
	return ''


@login_required
def home(request):

	unread_messages = Message.box.inbox_detailed_for(request.user)

	return render_to_response('home.html',
		{'unread_messages':unread_messages[1]},
		context_instance = RequestContext(request))

@login_required
def view_students(request, student_id = None, old_trail = None):

	#When a specific student is requested:
	if student_id != None:
		student = Student.objects.get(personid = student_id)
		profile_form = EditStudentProfileForm(instance = student)
		user_form = EditUserForm(instance = student.user)

		return render_to_response('student_profile.html',
				{'student':student,
				'profile_form':profile_form,
				'user_form':user_form},
			    context_instance = RequestContext(request))


	student_list = Student.objects.all()

	#Paginator handles displaying and changing between pages. Diplays
	#20 records at a time from the student_list queryset.
	paginator = Paginator(student_list, 20)


	page = request.GET.get('page')
	try:
		allstudents = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		allstudents = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		allstudents = paginator.page(paginator.num_pages)

	return render_to_response('students.html',
				{'allstudents':allstudents,
				'test':student_list},
			    context_instance = RequestContext(request))

def view_classes(request, student_id, action = None):

	"""Handles requests to view information on a student's all_classes
	and also handles actions when viewing classes"""

	completion_events_list = []
	code_list = []
	failed_list = []
	
	student = Student.objects.get(personid = student_id)


	if request.method == "POST":

		search_form = ClassSearchForm(request.POST)

		if search_form.is_valid():

			#Create list of individual codes <-->Strip all empty spaces
			#and create a new list <--> Remove blank entry at end of list 
			form_data = search_form.cleaned_data['new_classes'].split(',')

			for data in form_data:
				if len(data) > 1:
					code_list.append(data.strip())

			for code in code_list:
				try:
					new_class = Class.objects.get(code = code)
					new_class.students.add(student)

				except ObjectDoesNotExist:
					failed_list.append(code)

			all_classes = Class.objects.filter(students = student,
				is_active = True).order_by('start_date')


			completion_events = CompletionEvent.objects.filter(student = student)
			

			for event in completion_events:
				for member in all_classes:
					if event.for_class == member:
						completion_events_list.append(member.code)


				search_form = ClassSearchForm()

		return render(request, 'student_classes.html',
		{'student':student,
		'all_classes':all_classes,
		'completed_classes':completion_events_list,
		'form_data':code_list,
		'class_search_form': search_form})

	else:

		search_form = ClassSearchForm()

		student = Student.objects.get(personid = student_id)
		#If the action to add a class has been requested, add the student to
		#the class before searching db.


		all_classes = Class.objects.filter(students = student,
			is_active = True).order_by('start_date')


		completion_events = CompletionEvent.objects.filter(student = student)
		

		for event in completion_events:
			for member in all_classes:
				if event.for_class == member:
					completion_events_list.append(member.code)


			search_form = ClassSearchForm()


		#tags, in this case a list of all the products stored in the database.
		return render(request, 'student_classes.html',
			{'student':student,
			'all_classes':all_classes,
			'completed_classes':completion_events_list,
			'class_search_form': search_form})


def all_classes(request, action = None, pk = None):
	"""
	Allows users to view a list of all classes
	"""
	
	#If an action has been requested
	if action and pk != None:

		#Marks class as deactivated.
		if action == 'remove':
			target_class = Class.objects.get(pk = pk)
			target_class.deactivate()
			target_class.save()

	class_list = Class.objects.filter(is_active = True)

	#Paginator handles displaying and changing between pages. Diplays
	#20 records at a time from the student_list queryset.
	paginator = Paginator(class_list, 20)


	page = request.GET.get('page')
	try:
		all_classes = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		all_classes = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		all_classes = paginator.page(paginator.num_pages)

	return render_to_response('all_classes.html',
				{'all_classes':all_classes},
			    context_instance = RequestContext(request))

def all_courses(request, action = None, pk = None):
	"""
	Allows users to view a list of all classes
	"""
	
	#If an action has been requested
	if action and pk != None:

		#Marks class as deactivated.
		if action == 'remove':
			target_class = Course.objects.get(pk = pk)
			target_class.deactivate()
			target_class.save()

	course_list = Course.objects.filter(is_active = True)

	#Paginator handles displaying and changing between pages. Diplays
	#20 records at a time from the student_list queryset.
	paginator = Paginator(course_list, 20)


	page = request.GET.get('page')
	try:
		all_courses = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		all_courses = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		all_courses = paginator.page(paginator.num_pages)

	return render_to_response('all_courses.html',
				{'all_courses':all_courses},
			    context_instance = RequestContext(request))

def course_details(request, action = None, pk = None):

	"""Handles viewing detailed information on a specific courses."""

	if action and pk != None:
		target_course = Course.objects.get(pk=pk)
		subjects = target_course.subject_set.all()
		campuses = target_course.campuses.all()

		if action == 'edit':
			if request.method == 'POST':
				form = EditCourseForm(request.POST,
					instance = target_course)
				if form.is_valid():
					form.save()

					return render(request, 'course_details.html',
						{'form':form,
						'subjects':subjects,
						'campuses':campuses,
						'course':target_course})

				else:

					return render(request, 'course_details.html',
						{'form':form,
						'subjects':subjects,
						'campuses':campuses,
						'course':target_course})

			else:
				form = EditCourseForm(instance = target_course)

				return render(request, 'course_details.html',
				{'form':form,
				'subjects':subjects,
				'campuses':campuses,
				'course':target_course})
	
	target_course = Course.objects.get(pk = pk)
	subjects = target_course.subject_set.all()
	campuses = target_course.campuses.all()
	form = EditCourseForm(instance = target_course)

	return render(request, 'course_details.html',
	{'course':target_course,
	'campuses':campuses,
	'subjects':subjects,
	'form':form})


def class_details(request, action = None, pk = None):

	"""Handles viewing detailed information on a specific class."""

	if action and pk != None:
		target_class = Class.objects.get(pk=pk)
		target_students = target_class.students.all()
		target_teachers = target_class.teachers.all()

		if action == 'edit':
			if request.method == 'POST':
				form = EditClassForm(request.POST,
					instance = target_class)
				if form.is_valid():
					form.save()

					return render(request, 'class_details.html',
						{'form':form,
						'class':target_class,
						'students':target_students,
						'teachers':target_teachers})

				else:

					return render(request, 'class_details.html',
						{'form':form,
						'class':target_class,
						'students':target_students,
						'teachers':target_teachers})

			else:
				form = EditClassForm(instance = target_class)

				return render(request, 'class_details.html',
				{'form':form,
				'class':target_class,
				'students':target_students,
				'teachers':target_teachers})
	
	target_class = Class.objects.get(pk = pk)
	teachers = target_class.teachers.all()
	students = target_class.students.all()
	form = EditClassForm(instance = target_class)

	return render(request, 'class_details.html',
	{'class':target_class,
	'students':students,
	'teachers':teachers,
	'form':form})

def remove_class(request, pk):
	"""Handles marking a class as inactive"""

	target_class = Class.objects.get(pk = pk)
	target_class.deactivate()
