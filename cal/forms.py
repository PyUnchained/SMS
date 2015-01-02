from django import forms
from django.contrib.auth.models import User

from cal.models import Entry

class EventDayForm(forms.ModelForm):

	date = forms.DateTimeField()
	body = forms.CharField(max_length = 200, widget = forms.Textarea(
		attrs = {'class':'textarea-sm'}))
	time = forms.CharField()

	class Meta:
		model = Entry
		fields = ('title','snippet', 'remind')
