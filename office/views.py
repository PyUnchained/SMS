import operator
from itertools import chain
from django.db.models import Q
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from office.models import Student, Staff, Class

# Create your views here.
def search(request, pk = None):
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

		if criteria[0] == 'class':
			
			#search the records. Uses a generator function to
			#create query conditions for every value in the
			#search criterion
			result1 = Class.objects.filter(reduce(operator.and_,
				(Q(code__icontains = x) for x in criteria[1:])
				))
			result2 = Class.objects.filter(reduce(operator.and_,
				(Q(campus__name__icontains = x) for x in criteria[1:])
				))

			class_result = list(chain(result1, result2))

			return render_to_response('search-class.html',
				{'class_result': class_result,},
				context_instance = RequestContext(request))

		if criteria[0] == 'studentaddclass':
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


			#Id's are searched separately, because matches for ids
			#are displayed differently to matches for the name
			id_result = Student.objects.filter(reduce(operator.and_,
				(Q(personid__icontains = x) for x in criteria[1:])
				))

			if pk != None:
				target_class = Class.objects.get(pk=pk)

				return render(request,'search-results-add-class.html',
				{'id_result': id_result,
				'name_result': name_result,
				'test':criteria,
				'class':target_class})

		if criteria[0] == 'teacheraddclass':
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


			#Id's are searched separately, because matches for ids
			#are displayed differently to matches for the name
			id_result = Staff.objects.filter(reduce(operator.and_,
				(Q(personid__icontains = x) for x in criteria[1:])
				))

			target_class = Class.objects.get(pk=pk)

			return render(request,'search-results-add-class.html',
			{'id_result': id_result,
			'name_result': name_result,
			'test':criteria,
			'class':target_class})


	#if nothing was typed, return no results
	else:
		id_result = None
		name_result = None
		

	return render_to_response('search-results.html',
			{'id_result': id_result,
			'name_result': name_result,
			'test':criteria},
			context_instance = RequestContext(request))

def PersonToClass(request):

	
	info = request.POST.get('info')
	info_list = str(info).split(',')
	target_class = Class.objects.get(pk = int(info_list[1]))

	try:
		student = Student.objects.get(personid = info_list[0])
		target_class.students.add(student)
		name = student.user.first_name + ' ' + student.user.last_name

	except ObjectDoesNotExist:
		teacher = Staff.objects.get(personid = info_list[0])
		target_class.teachers.add(teacher)
		name = teacher.user.first_name + ' ' + teacher.user.last_name
	
	

	# Generate success message
	class_name = str(target_class.code)
	response = name + ' has been added to class '
	response = response + class_name + ' successfully!\n\n'
	response = response + 'Reload page to view updates.'



	return render(request, 'popupmsg.html',
		{'test':response})




