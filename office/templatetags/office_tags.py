from django import template
from office.models import Student

register = template.Library()



def all_studentslist():
	students = Student.objects.all()
	return {'students':students}


register.inclusion_tag('student_list.html')(all_studentslist)