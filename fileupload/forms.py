from django import forms
from django.contrib.auth import get_user_model

attrs_dict = {'class': 'required', 'maxlength':256}

class CreateUserForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs=attrs_dict))
	password1 = forms.CharField(widget=forms.TextInput(attrs=attrs_dict))
	password2 = forms.CharField(widget=forms.TextInput(attrs=attrs_dict))

	def clean_username(self):
		""" Validate that the username is alphanumeric and is not alreadyin use. """
		existing = get_user_model().objects.filter(username__iexact=self.cleaned_data['username'])
		if existing.exists():
			raise forms.ValidationError("A user with that username already exists.")
		else:
			return self.cleaned_data['username']


	def clean(self):
		""" Verifiy that the values entered into the two password fields
		match. Note that an error here will end up in
		non_field_errors()`` because it doesn't apply to a single field.
		"""
		
		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
			if self.cleaned_data['password1'] != self.cleaned_data['password2']:
				raise forms.ValidationError("The two password fields didn't match.")
		return self.cleaned_data