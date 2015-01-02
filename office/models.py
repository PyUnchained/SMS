import uuid #Used to generate random ids.
import datetime

from django.contrib import admin
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


def generateid(first, middle, last, type = None):
		""" Generates an id in the form of:

		[initials][registration_year][number]

		Takes the first, middle and last names as arguments, in that order.

		"""

		#Identify and form initials.
		initials = ''
		names = (first, middle, last)
		for name in names:
			initials = initials + name[:1].upper()

		#Find year.
		year = str(datetime.date.today().year)
		year = year[2:]

		#Find number
		student_num = Student.objects.all().count()
		staff_num = Staff.objects.all().count()

		number = str(student_num + staff_num)

		#Form id
		newid = initials + year + number

		return newid
	



class CommonInfo(models.Model):
	"""Stores information relating to all users."""

	SEX_CHOICES = (
        ('M','Male'),
        ('F','Female'),
    )

	personid = models.CharField(max_length = 20, primary_key = True,
		unique = True, blank = True)
	system_id = models.CharField(max_length = 36,
		default = uuid.uuid4, editable = False)

	user = models.ForeignKey(User, unique = True, null = True)

	name = models.CharField(max_length = 50)
	middle_name = models.CharField(max_length = 100, default = '')
	surname = models.CharField(max_length = 50)
	sex = models.CharField('sex',max_length=1, choices=SEX_CHOICES)
	date_of_birth = models.DateField('date of Birth')
	national_id = models.CharField('National ID/Passport No.',
		max_length = 50, unique = True)
	pic = models.FileField('Profile Picture',
		upload_to = 'office/profile_pics/%Y/')

	card_id = models.CharField('Card ID', max_length = 36,
		default = uuid.uuid4)
	account_id = models.CharField('Account ID', max_length = 20)

	is_active = models.BooleanField(default = True)


	billing_address_street = models.CharField('Billing Address (Number/Street)',
    	max_length=50)
	billing_address_city = models.CharField('city',max_length=50)
	billing_address_country = models.CharField('country',max_length=50)
	homephone = models.CharField('home Phone',max_length=20)
	preffered_cell = models.CharField('cellphone',
    	max_length=50,
    	help_text = 'Your preferred cellphone number to use.')
	secondary_cell = models.CharField('cellphone',
    	max_length=50, blank = True,
    	help_text = 'Your secondary cellphone number.')
	tertiary_cell = models.CharField('cellphone',
    	max_length=50, blank = True,
    	help_text = 'Your tertiary cellphone number.')
	email2 = models.EmailField('Secondary Email', max_length=50,
		blank=True,
		help_text = 'Your secondary e-mail.')
	skype = models.CharField('skype Name',max_length=50, blank=True)
	registration_date = models.DateField(auto_now_add = True)


	def deactivate(self):
		self.is_active == False
		return self.is_active

	def activate(self):
		self.is_active == True
		return self.is_active

	def __str__(self):
		return ' '.join([
			self.name,
			self.surname
			])

	class Meta:
		abstract = True

class Student(CommonInfo):
	"""Stores information specific to students."""

	is_overdue = models.BooleanField(default=False)
	books = models.CharField(max_length = 6, default = 'IE')

	class Admin():
	    pass

	def save(self, *args, **kwargs):
		if not self.personid:
			self.personid = generateid(self.name, self.middle_name, self.surname)

		super(Student, self).save( *args, **kwargs)



class Staff(CommonInfo):
	"""Stores information specific to staff."""

	ROLE_CHOICES = (
		('L','Lecturer'),
		('LA','Low Level Admin'),
		('HA','High Level Admin'),
		('FA','Full Admin')
	)

	role = models.CharField('Role',max_length=2, choices=ROLE_CHOICES)
	is_on_leave = models.BooleanField(default = False)
	contract = models.FileField('Contract File',
		upload_to = 'office/staff/contracts/%Y/')
	books = models.CharField(max_length = 6, default = 'IE')


	class Admin():
	    pass

	class Meta:
		verbose_name_plural = 'staff'

	def save(self, *args, **kwargs):
		if not self.personid:
			self.personid = generateid(self.name, self.middle_name, self.surname)
		super(Saff, self).save( * args, ** kwargs)

class Campus(models.Model):
	"""Represents information pertinent to a specific campus."""

	code = models.CharField(max_length = 8)
	name = models.CharField(max_length = 50)
	official_name = models.CharField(max_length = 50)
	address = models.CharField(max_length = 50)
	email = models.EmailField()
	website = models.URLField()

	def print_class():
		return self.name

	def __str__(self):
		return self.official_name

	class Meta:
		verbose_name_plural = 'campuses'

	class Admin():
	    pass

class Course(models.Model):
	"""Represents information pertinent to a specific course."""

	code = models.CharField(max_length = 8, primary_key = True)

	title = models.CharField(max_length = 100)
	subtitle = models.CharField(blank = True, max_length = 100)
	syllabus_code = models.CharField(max_length = 50)

	campuses = models.ManyToManyField(Campus)

	price = models.PositiveIntegerField()
	duration = models.PositiveSmallIntegerField(help_text = 'Duration in weeks')

	is_active = models.BooleanField(default = True)

	def __str__(self):
		return '{} ({})'.format(self.title, self.syllabus_code)

	def print_class():
		return self.title



	class Admin():
	    pass

class Class(models.Model):
	"""Represents information pertinent to a specific class."""

	code = models.CharField(max_length = 8, primary_key = True)

	teachers = models.ManyToManyField(Staff)
	students = models.ManyToManyField(Student)
	course = models.ForeignKey(Course)
	campus = models.ForeignKey(Campus)
	start_date = models.DateField()
	exam_date = models.DateField(blank = True, null = True)
	min_students = models.PositiveSmallIntegerField(blank = True)
	max_students = models.PositiveSmallIntegerField(blank = True)

	schedule = models.FileField(blank = True, upload_to = 'office/schedules/%m/')

	is_active = models.BooleanField(default = True)

	def __str__(self):

		return '{} {} : {}'.format(self.course.syllabus_code,
			self.start_date,
			self.campus.official_name)

	class Meta:
		verbose_name_plural = 'classes'

	class Admin():
	    pass


class Subject(models.Model):
	"""Stores information about a specific subject"""

	id = models.CharField(max_length = 8, primary_key = True)

	title = models.CharField(max_length = 100)
	subtitle = models.CharField(blank = True, max_length = 100)
	subject_code = models.CharField('Subject Code',
		max_length = 50)
	description = models.TextField('Description',
		max_length = 300)

	courses = models.ManyToManyField(Course)

	def __str__(self):
		return self.title


	class Admin():
	    pass

class Result(models.Model):
	"""Stores the mark each student has obtained for each assignment"""

	student = models.ForeignKey(Student)
	percent_grade = models.PositiveSmallIntegerField(blank = True,
		null = True)
	value_grade = models.PositiveSmallIntegerField(blank = True,
		null = True)





class CommonAction(models.Model):
	"""Lists commonly carried out actions and their URLs"""

	name = models.CharField(max_length= 50)
	page = models.URLField()

	def __str__(self):
		return self.name

	class Admin():
	    pass

admin.site.register(Subject)
admin.site.register(Class)
admin.site.register(Course)
admin.site.register(Campus)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(CommonAction)