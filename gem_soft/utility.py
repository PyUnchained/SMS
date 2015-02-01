from django.core.urlresolvers import reverse, resolve
from sms.settings import BASE_DIR
import imp
import sys
import os

def previous_url(request):
	"""Takes a request object and returns the previous url in a form that
	the builtin django reverse and resolver functions can use."""
	
	try:
		small_url = request.META['HTTP_REFERER']

		#Loop through the url to find the third /, denoting the url
		#without the server part(which can't be recognized by resolver).
		num = 0
		index = 0
		for char in small_url:
			if char == '/':
				num += 1
			if num == 3:
				target_index = index
				break
			index += 1

		#Represents the shortened url.
		small_url = small_url[target_index:]

		#Get the reverse url value
		reverse_url = resolve(small_url)
		url_kwargs = reverse_url.kwargs
		url_name = reverse_url.url_name
		small_url = reverse(url_name,kwargs=url_kwargs)

		return small_url

	except KeyError:
		return None

def dynamic_import(name, globals=None, locals=None, fromlist=None):
    # Fast path: see if the module has already been imported.
    try:
        return sys.modules[name]
    except KeyError:
        pass

    # If any of the following calls raises an exception,
    # there's a problem we can't handle -- let the caller handle it.

    fp, pathname, description = imp.find_module(name)

    try:
        return imp.load_module(name, fp, pathname, description)
    finally:
        # Since we may exit via an exception, close fp explicitly.
        if fp:
            fp.close()

def find_modules(name, extension = None):
	"""
	Returns a list of strings for all django modules of a specific type.
	An example of its usage would be to return the models module of every
	app in the project folder by finding all models.py files.
	
	Args:
		name: desired filename to search for

	Returns:
		A list of strings representing the names of the target modules.
		e.g.:

		['first.module','second.module']
	"""

	name = str(name)

	#Chack that the .py extenstion was added, add it if it is not.
	if '.py' not in name:
		if extension != None:
			name = name + str(extension)
		else:	
			name = name + '.py' #If no extension given, assume .py

	result = []
	for root, dirs, files in os.walk(BASE_DIR):
		if name in files:
			raw = os.path.join(root, name)
			raw = raw.split('/')
			output = raw[-2] + '.' + raw[-1]
			result.append(output[:-3])
	return result
