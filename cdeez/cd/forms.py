from django import forms

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

class LoginForm(forms.Form):
	username = forms.CharField(label = 'Username', required = True)
	password = forms.CharField(label = 'Password', widget = forms.PasswordInput(), required = True)

class CreateUser(forms.Form):
	username = forms.CharField(label = 'Username', required = True)
	email = forms.EmailField(label = 'Email', required = True)
	password = forms.CharField(label = 'Password', widget = forms.PasswordInput(), required = True)
	password_verify = forms.CharField(label = 'Password', widget = forms.PasswordInput(), required = True)

class MajorForm(forms.Form):
	major = forms.CharField(label = 'Major', required = True)
