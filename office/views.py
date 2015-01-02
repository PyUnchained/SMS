import operator
from itertools import chain
from django.db.models import Q
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User

from office.models import Student, Staff

# Create your views here.
def search(request):
	"""
	Receives a string called question containing search terms
	separated by hyphens, searches the database and returns the
	results.
	"""
	question = request.GET.get('q')
	criteria = question.split('-')
	#check that something has actually been typed
	if criteria[1] != '':

		#after spliting up the search terms, identify the prefix
		#and search through the appropriate records as needed
		if criteria[0] == 'student':

			#search the records. Uses a generator function to
			#create query conditions for every value in the
			#search criterion
			result1 = Student.objects.filter(reduce(operator.and_,
				(Q(user__first_name__icontains = x) for x in criteria[1:])
				))
			result2 = Student.objects.filter(reduce(operator.and_,
				(Q(user__last_name__icontains = x) for x in criteria[1:])
				))

			name_result = list(chain(result1, result2))


			#since the id is only found in the student profiles
			#it is searched separately.
			id_result = Student.objects.filter(reduce(operator.and_,
				(Q(personid__icontains = x) for x in criteria[1:])
				))


		if criteria[0] == 'staff':
			
			#search the records. Uses a generator function to
			#create query conditions for every value in the
			#search criterion
			result1 = Staff.objects.filter(reduce(operator.and_,
				(Q(user__first_name__icontains = x) for x in criteria[1:])
				))
			result2 = Staff.objects.filter(reduce(operator.and_,
				(Q(user__last_name__icontains = x) for x in criteria[1:])
				))

			name_result = list(chain(result1, result2))


			#since the id is only found in the student profiles
			#it is searched separately.
			id_result = Staff.objects.filter(reduce(operator.and_,
				(Q(personid__icontains = x) for x in criteria[1:])
				))


	#if nothing was typed, return no results
	else:
		id_result = None
		name_result = None
		

	return render_to_response('search-results.html',
			{'id_result': id_result,
			'name_result': name_result,
			'test':criteria},
			context_instance = RequestContext(request))

