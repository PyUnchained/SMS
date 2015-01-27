from django.core.urlresolvers import reverse, resolve

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