import operator
from itertools import chain
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from bookkeep.models import*
from office.models import*
from cal.models import*
from msg_box.models import*
from sms_admin.models import*

def lookup_staff(terms):

	#search the records. Uses a generator function to
	#create query conditions for every value in the
	#search criterion

	result1 = Staff.objects.filter(reduce(operator.and_,
		(Q(user__first_name__icontains = x) for x in terms)
		))

	result2 = Staff.objects.filter(reduce(operator.and_,
		(Q(user__last_name__icontains = x) for x in terms)
		))

	result3 = Staff.objects.filter(reduce(operator.and_,
		(Q(middle_name__icontains = x) for x in terms)
		))

	name_result = list(chain(result1, result2, result3))


	#Id's are searched separately, because matches for ids
	#are displayed differently to matches for the name
	id_result = Staff.objects.filter(reduce(operator.and_,
		(Q(personid__icontains = x) for x in terms)
		))

	return (name_result,id_result)

def lookup_students(terms):

	#search the records. Uses a generator function to
	#create query conditions for every value in the
	#search criterion

	result1 = Student.objects.filter(reduce(operator.and_,
		(Q(user__first_name__icontains = x) for x in terms)
		))

	result2 = Student.objects.filter(reduce(operator.and_,
		(Q(user__last_name__icontains = x) for x in terms)
		))

	result3 = Student.objects.filter(reduce(operator.and_,
		(Q(middle_name__icontains = x) for x in terms)
		))

	name_result = list(chain(result1, result2, result3))


	#Id's are searched separately, because matches for ids
	#are displayed differently to matches for the name
	id_result = Student.objects.filter(reduce(operator.and_,
		(Q(personid__icontains = x) for x in terms)
		))

	return (name_result,id_result)


def lookup_subjects(terms):
	#search the records. Uses a generator function to
	#create query conditions for every value in the
	#search criterion
	result1 = Subject.objects.filter(reduce(operator.and_,
		(Q(title__icontains = x) for x in terms)
		))

	result2 = Subject.objects.filter(reduce(operator.and_,
		(Q(subtitle__icontains = x) for x in terms)
		))

	name_result = list(chain(result1, result2))


	#Id's are searched separately, because matches for ids
	#are displayed differently to matches for the name
	id_result = Subject.objects.filter(reduce(operator.and_,
		(Q(subject_code__icontains = x) for x in terms)
		))

	return (name_result,id_result)

def lookup_courses(terms):
	#search the records. Uses a generator function to
	#create query conditions for every value in the
	#search criterion
	result1 = Course.objects.filter(reduce(operator.and_,
		(Q(title__icontains = x) for x in terms)
		))

	result2 = Course.objects.filter(reduce(operator.and_,
		(Q(subtitle__icontains = x) for x in terms)
		))

	name_result = list(chain(result1, result2))


	#Id's are searched separately, because matches for ids
	#are displayed differently to matches for the name
	id_result = Course.objects.filter(reduce(operator.and_,
		(Q(syllabus_code__icontains = x) for x in terms)
		))

	return (name_result,id_result)

def campus_lookup(terms):
	#search the records. Uses a generator function to
	#create query conditions for every value in the
	#search criterion
	result1 = Campus.objects.filter(reduce(operator.and_,
		(Q(name__icontains = x) for x in terms)
		))

	result2 = Campus.objects.filter(reduce(operator.and_,
		(Q(official_name__icontains = x) for x in terms)
		))

	result3 = Campus.objects.filter(reduce(operator.and_,
		(Q(address__icontains = x) for x in terms)
		))

	result = list(chain(result1, result2, result3))

	return (result)