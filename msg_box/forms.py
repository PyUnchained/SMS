from django import forms
from django.contrib.auth.models import User

from msg_box.models import Message

class ComposeForm(forms.ModelForm):

	new_recepients = forms.CharField(max_length = 300, widget=forms.Textarea)
	
	class Meta:
		model = Message
		fields = ('title','body')
