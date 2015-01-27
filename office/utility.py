from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse, resolve

from office.models import*

def RemoveSubjectFromCourse(subject_pk, course_pk):

	try:
		target_subject = Subject.objects.get(pk=subject_pk)
		target_course = Course.objects.get(pk = course_pk)
		subject.courses.remove(target_course)
		return True

	except ObjectDoesNotExist:
		return False