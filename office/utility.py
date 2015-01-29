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
		#Check to see that a student is being added to the class
		if isinstance(extra_obj, Student):
			obj.students.add(extra_obj)
			obj.save()
			return "Added Student to Class"

		#Check to see that a teacher is being added to the class
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