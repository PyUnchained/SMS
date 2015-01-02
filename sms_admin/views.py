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
		student = Student.objects.get(pk = student_id)
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