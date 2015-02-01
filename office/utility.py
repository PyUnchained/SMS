from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse, resolve

from office.models import*
from bookkeep.models import*
from cal.models import*
from msg_box.models import*
from sms_admin.models import*

def RemoveSubjectFromCourse(subject_pk, course_pk):

	try:
		target_subject = Subject.objects.get(pk=subject_pk)
		target_course = Course.objects.get(pk = course_pk)
		subject.courses.remove(target_course)
		return True

	except ObjectDoesNotExist:
		return False

def add_to(obj, extra_obj):

	if isinstance(obj, Class):
		#Check to see where it is being added and perform the appropriate
		#action
		if isinstance(extra_obj, Student):
			obj.students.add(extra_obj)
			obj.save()
			return "Added Student to Class"

		if isinstance(extra_obj, Staff):
			obj.teachers.add(extra_obj)
			obj.save()
			return "Added Teacher to Class"

		error_msg = 'An error occurred adding {} to Class'.format(
			type(extra_obj).__name__)
		return error_msg

	elif isinstance(obj,Course):

		if isinstance(extra_obj, Campus):
			obj.campuses.add(extra_obj)
			obj.save()
			return "Added Teacher to Class"

		if isinstance(extra_obj, Subject):
			obj.subjects.add(extra_obj)
			obj.save()
			return "Added Teacher to Class"

		error_msg = 'An error occurred adding {} to course'.format(
					type(extra_obj).__name__)
		return error_msg

	elif isinstance(obj, Assignment):

		if isinstance(extra_obj, Class):
			obj.classes.add(extra_obj)
			obj.save()
			return "Added Teacher to Class"

		error_msg = 'An error occurred adding {} to course'.format(
					type(extra_obj).__name__)
		return error_msg

	else:

		return False

def remove_from(obj, extra_obj):

	if isinstance(obj, Class):
		if isinstance(extra_obj, Student):
			obj.students.remove(extra_obj)
			obj.save()
			return "Removed Student from Class"

		if isinstance(extra_obj, Staff):
			obj.teachers.remove(extra_obj)
			obj.save()
			return "Removed Teacher from Class"

		error_msg = 'An error occurred removing {} from Class'.format(
			type(extra_obj).__name__)
		return error_msg

	elif isinstance(obj,Course):
		if isinstance(extra_obj, Campus):
			obj.campuses.remove(extra_obj)
			obj.save()
			return "Removed Teacher from Class"

		if isinstance(extra_obj, Subject):
			obj.subjects.remove(extra_obj)
			obj.save()
			return "Removed Teacher from Class"

		error_msg = 'An error occurred removing {} from course'.format(
					type(extra_obj).__name__)
		return error_msg

	elif isinstance(obj, Assignment):
		if isinstance(extra_obj, Class):
			obj.classes.remove(extra_obj)
			obj.save()
			return "Removed Teacher from Class"

		error_msg = 'An error occurred removing {} from course'.format(
					type(extra_obj).__name__)
		return error_msg

	else:

		return False