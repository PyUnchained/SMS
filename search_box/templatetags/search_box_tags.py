from django import template
from office.models import*
from bookkeep.models import*
from cal.models import*
from msg_box.models import*
from sms_admin.models import*

register = template.Library()


@register.inclusion_tag('view_search.html', takes_context=True)
def view_search(context, obj):

	if isinstance(obj, Student):
		input_id = 'view-students'
		result_id = input_id + '-result'		

	elif isinstance(obj, Staff):
		input_id = 'view-staff'
		result_id = input_id + '-result'

	elif isinstance(obj, Course):
		input_id = 'view-courses'
		result_id = input_id + '-result'

	elif isinstance(obj, Subject):
		input_id = 'view-subjects'
		result_id = input_id + '-result'

	return {'input_id':input_id,
			'result_id': result_id}