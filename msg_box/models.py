from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
# Create your models here.

class MessagesManager(models.Manager):

	"""
	Adds a 'box' class to Message objects, eg - Messages.box.inbox_for([user])

	"""

	def inbox_for(self, current_user):
		""" Returns all the messages sent to a specific user """

		return self.filter(Q(recepients = current_user),
			~Q(deleted_by = current_user)).order_by('sent_on')

	def inbox_detailed_for(self, current_user):
		""" Returns a tuple of all the inbox messages and the total number
		of messages."""

		queryset = self.inbox_for(current_user)

		unread_count = 0
		for item in queryset:
			if item.read_on == None:
				unread_count += 1

		return (queryset,unread_count) 

	def sentbox_for(self, current_user):
		""" Returns all the messages sent by a specific user """

		return self.filter(sender = current_user)

	def trashbox_for(self, current_user):
		""" Returns all messages deleted by a specific user """

		return self.filter(deleted_by = current_user)

	def retrieve(self, pk):
		""" Returns all messages deleted by a specific user """

		return self.get(pk = pk)


class Message(models.Model):

	title = models.CharField(max_length = 50)
	body = models.TextField(max_length = 1000)
	sender = models.ForeignKey(User, related_name = '+')
	recepients = models.ManyToManyField(User)

	sent_on = models.DateTimeField(auto_now_add = True)
	read_on = models.DateTimeField(blank = True, null = True)
	replied_on = models.DateTimeField(blank = True, null = True)
	forwarded_on = models.DateTimeField(blank = True, null = True)

	reply_to_message = models.ForeignKey('self',
		blank = True,
		null = True,
		related_name = 'reply_to')

	deleted_by = models.ManyToManyField(User,
		related_name = 'deleted_by_user',
		blank = True, null = True)

	deleted = models.BooleanField(default = False)
	objects = models.Manager()

	box = MessagesManager()

	def delete(self, current_user):
		self.deleted_by.add(current_user)
		return True

	class Admin():
	    pass

def inbox_count_for(current_user):
	"""
	Returns the number of unread messages currently in the inbox.

	"""

	return Message.objects.filter(Q(recepients = current_user),
		~Q(deleted_by = current_user)).count()

admin.site.register(Message)