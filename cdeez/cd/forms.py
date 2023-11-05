from django import forms
from .utils import Driver


# class CharField(forms.CharField):
# 	def __init__(self, widget = forms.TextInput(), required = False, **kwargs):
# 		kwargs['widget'] = widget
# 		kwargs['required'] = required
# 		super(CharField, self).__init__(**kwargs)

# class TextField(forms.CharField):
# 	def __init__(self, widget = forms.Textarea(), required = False, **kwargs):
# 		kwargs['widget'] = widget
# 		kwargs['required'] = required
# 		super(TextField, self).__init__(**kwargs)

class BooleanField(forms.BooleanField):
	def __init__(self, widget = forms.CheckboxInput(attrs = {"class":"test","onclick": "post()"}), required = False, **kwargs):
		kwargs['widget'] = widget
		kwargs['required'] = required
		super(BooleanField, self).__init__(**kwargs)

driver = Driver()

class LoginForm(forms.Form):
	username = forms.CharField(label = 'Username', required = True)
	password = forms.CharField(label = 'Password', widget = forms.PasswordInput(), required = True)

class CreateUser(forms.Form):
	username = forms.CharField(label = 'Username', required = True)
	email = forms.EmailField(label = 'Email', required = True)
	password = forms.CharField(label = 'Password', widget = forms.PasswordInput(), required = True)
	password_verify = forms.CharField(label = 'Password', widget = forms.PasswordInput(), required = True)

class MajorForm(forms.Form):
	def __init__(self, choices, *args, **kwargs):
		super(MajorForm, self).__init__(*args, **kwargs)
		self.fields['major'] = forms.ChoiceField(choices=choices, widget=forms.Select(attrs={'class': 'form-control'}), required=True)

class CompletionForm(forms.Form):
	def __init__(self, courses, *args, **kwargs):
		super(CompletionForm, self).__init__(*args, **kwargs)
		for i in courses:
			self.fields[i] = BooleanField()