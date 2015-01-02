import re

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from office.models import Student, Staff

from msg_box.models import Message
from msg_box.forms import ComposeForm

# Create your views here.

@login_required
def inbox(request):
	""" 
	Shows all read and unread messages sent to a user.
	"""
	inbox, count = Message.box.inbox_detailed_for(request.user)

	return render_to_response('msg_box_box.html',
		{'box':inbox,
		'inbox_count':count,
		'box_name':'Inbox'},
		context_instance = RequestContext(request))

@login_required
def sentbox(request):
	""" 
	Shows all messages sent by a user.
	"""
	box = Message.box.sentbox_for(request.user)

	return render_to_response('msg_box_box.html',
		{'box':box,
		'box_name':'Sent Messages'},
		context_instance = RequestContext(request))

@login_required
def trashbox(request):
	""" 
	Shows all messages 'deleted' by a user.
	"""
	box = Message.box.trashbox_for(request.user)

	return render_to_response('msg_box_box.html',
		{'box':box,
		'box_name':'Trash'},
		context_instance = RequestContext(request))

@login_required
def compose(request, reply_pk = None, mode = None):
	""" 
	Displays a simple form allowing users to send a message.

	The reply_pk variable represents the pk for the user to respond
	to when users reply a specific message.

	"""
	current_user = request.user

	if request.method == "POST":
		form = ComposeForm(request.POST)

		recepient_check = send_to(request.POST['new_recepients'])
        
		if form.is_valid():


			#If the form is valid, collect the information from the
			#ComposeForm, create a new Message object and save it.
			allclean = form.cleaned_data

			

			#Since recepients is a many-to-many relationship...
			#First create message object without the m2m
			#relationship
			new_message = Message.objects.create(title = allclean['title'],
				body = allclean['body'],
				sender = current_user)

			#Then add each m2m relationship by looping through all
			#intended recepients. Identify any recepients that have
			#been incorrectly entered in the process
			failed_list = []
			for identifier in recepient_check:
				#First look for students
				try:
					person = Student.objects.get(personid = identifier)
					new_message.recepients.add(person.user)
				except ObjectDoesNotExist:
					#If it's not a student, try the staff
					try:
						person = Staff.objects.get(personid = identifier)
						new_message.recepients.add(person.user)
					except ObjectDoesNotExist:

						#If the objects still doesn't exist, assume it
						#was typed incorrectly
						failed_list.append(identifier)

			#If there are any incorrect recepients display a warning
			#and do not send.
			if len(failed_list) >= 1:
				return render_to_response('msg_box_compose.html',
			    {'form':form,
			    'recepients_warning':failed_list},
			    context_instance = RequestContext(request))



			#If the current message is a reply, indicate which message 
			#the current one is a reply to.
			if reply_pk:
				new_message.reply_to_message = Message.objects.get(
					pk = reply_pk)

			new_message.save()

			#Return to the inbox with a success message
			current_user = request.user
			inbox, count = Message.box.inbox_detailed_for(current_user)

			form = ComposeForm()

			return render_to_response('msg_box_compose.html',
				{'box':inbox,
				'form':form,
				'success_message':'Message Sent',
				}, #success message
				context_instance = RequestContext(request))

		else:            
			return render_to_response('msg_box_compose.html',
			    {'form':form,},
			    context_instance = RequestContext(request))

	else:
		if reply_pk:

			#change message title depending on whether it is a forward
			#or a reply
			if mode == 'fwd':
				message = Message.objects.get(pk = reply_pk,
					recepients = current_user)
				new_title = 'Fwd: ' + message.title
				form = ComposeForm(initial = {'title':new_title})

			elif mode == 're':
				message = Message.objects.get(pk = reply_pk,
					recepients = current_user)
				new_title = 'Re: ' + message.title
				form = ComposeForm(initial = {'title':new_title})

			elif mode == 'new':
				reply_pk = reply_pk + ','
				form = ComposeForm(initial = {'new_recepients':reply_pk})

			



		else:
			form = ComposeForm()

		return render_to_response('msg_box_compose.html',
                {'form':form,
                'send_to_id':reply_pk},
                context_instance = RequestContext(request))


@login_required
def view_message(request, message_pk):
	""" Returns the details of a single message """

	current_user = request.user
	try:
		message = Message.objects.get(pk = message_pk,
			recepients = current_user)
	except ObjectDoesNotExist:
		message = Message.objects.get(pk = message_pk,
			sender = current_user)

	return render_to_response('msg_box_view.html',
		{'message':message,},
		context_instance = RequestContext(request))


	
@login_required
def delete_message(request, message_pk):
	""" Returns the details of a single message """

	current_user = request.user
	message = Message.objects.get(pk = message_pk,
		recepients = current_user)

	message.delete(current_user)

	return redirect('msg_box_inbox')


def send_to(recepient_string):
	"""
	Takes a comma seprated string of recepient ids and returns the recepients
	as a list, removing duplicates in the process.

	"""

	recepient_list = recepient_string.split(',')
	repeat_list = []
	for recepient in recepient_list:
		if len(recepient) > 1:

			#look for tags denoting the name of a recepient and remove
			#them
			if '<' in recepient:
				char_index = recepient.index('<')
				recepient = recepient[:char_index]
				repeat_list.append(recepient.strip())

	#Remove duplicate recepients
	final_list = []
	for recepient in repeat_list:
		if recepient not in final_list:
			final_list.append(recepient)

	return final_list