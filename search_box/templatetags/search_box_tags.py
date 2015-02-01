from django import template
from office.models import*
from bookkeep.models import*
from cal.models import*
from msg_box.models import*
from sms_admin.models import*

register = template.Library()


@register.inclusion_tag('search.html')
def view_search(obj):
	"""
	Creates a template for a search-box that allows users to view
	individual records.

	Args:
		obj: instance of the target model to search the db for.

	Returns:
		A template for the search-box with a suitable id to identify it in
		subesequent get requests.

	"""

	input_class = 'search-input'

	if isinstance(obj, Student):
		input_id = 'view-' +type(obj).__name__
		result_id = input_id + '-result'		

	elif isinstance(obj, Staff):
		input_id = 'view-' +type(obj).__name__
		result_id = input_id + '-result'

	elif isinstance(obj, Course):
		input_id = 'view-' +type(obj).__name__
		result_id = input_id + '-result'

	elif isinstance(obj, Subject):
		input_id = 'view-' +type(obj).__name__
		result_id = input_id + '-result'

	return {'input_id':input_id,
			'result_id': result_id,
			'class':input_class}

@register.inclusion_tag('search.html')
def add_search(obj):
	"""
	Creates a template for a search-box that allows users to add
	relationships between two specific records.

	Args:
		obj: instance of the target model to add to the db.

	Returns:
		A template for the search-box with a suitable id to identify it in
		subesequent get requests.

	"""
	input_class = 'search-input'
	specific_obj = type(obj).__name__
	specific_obj = specific_obj + str(obj.pk)

	input_id = 'add-' + specific_obj
	result_id = input_id + '-result'		

	return {'input_id':input_id,
			'result_id': result_id,
			'class':input_class}