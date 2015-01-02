from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q

class JournalManager(models.Manager):

	def get_books_all(self, account_num, db_map = None):
		"""
		Finds all entries in all books for a specific account.
		Entries are stored as a list for each book.
		All the books found are then returned in a dictionary

		account_num - account number to find books for.

		books - list of books and their mapping in the db.

		"""

		if db_map == None:
			db_map = (
				('I', 'Income'),
				('E', 'Expenditure'),
				('P', 'Payments'),
				('R', 'Rebates'),
				('S', 'Salaries'),
				('D', 'Deductions'))

		books = {}
		#populate the books dictionary with the books provided
		#in the mapping.
		for mapping in db_map:
			db_value, new_key = mapping
			books[new_key] = []


		#Get a list of all available entries ordered by date
		all_entries = self.filter(account_num = account_num).order('date')

		#add each entry to the appropriate list in books
		for entry in all_entries:
			for mapping in db_map:
				db_id, name = mapping

				#if the book the entry was recorded for matches the current
				#entry, append it to the appropriate list.
				if entry.book == db_id:
					books[name].append(entry)

		return books


class JournalEntry(models.Model):

	METHODS = (
		('C','Cash'),
		('CR', 'Credit'),
		('EFT', 'Electronic Fund Transfer'),
		('ECO', 'EcoCash'))

	DESCRIPTIONS = (
		('0','No Descriptions Loaded'),)

	BOOKS = (
		('I', 'Income'),
		('E', 'Expenditure'),
		('P', 'Payments'),
		('R', 'Rebates'),
		('S', 'Salaries'),
		('D', 'Deductions'))

	account_user = models.ForeignKey(User, primary_key = False)
	account_num = models.CharField(max_length = 20)
	book = models.CharField(max_length = 3, choices = BOOKS)
	payment_method = models.CharField(max_length = 3, choices = METHODS)
	standard_description = models.CharField(max_length = 3,
		choices = DESCRIPTIONS,
		blank = True)
	custom_description = models.CharField(max_length = 150,
		blank = True,
		default = '')
	date = models.DateField()
	amount = models.DecimalField(max_digits=17, decimal_places=2)
	ref_number = models.CharField(max_length = 20)
	recorded_by = models.OneToOneField(User, related_name = 'recording_user')
	recorded_on = models.DateTimeField(auto_now_add = True)

	objects = models.Manager()
	books = JournalManager()

	def save(self, *args, **kwargs):
		if not self.ref_number:
			self.ref_number = generate_ref(self.payment_method,
				self.standard_description,
				self.custom_description)
		super(JournalEntry, self).save( *args, **kwargs)

class EntryDescription(model.Models):
	text = models.CharField(max_length = 150)

class JournalBook(model.Models):
	db_id = models.CharField(max_length = 2)
	name = models.CharField(max_length = 150)

def generate_ref(payment_method, standard_description, custom_description):
	"""Generates a unique reference number for each entry."""

	num = JournalEntry.objects.all.count()
	ref = payment_method + str(num) + standard_description + custom_description
	return ref
