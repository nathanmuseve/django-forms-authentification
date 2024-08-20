from django  import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
  email = forms.EmailField(widget=forms.EmailInput)
  password = forms.CharField(widget=forms.PasswordInput)
  password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
  
  class Meta:
    model = User
    fields = ['username', 'password', 'password_confirm']
    
    #aunthentification logic
  def clean(self):
    cleaned_data = super().clean()
    email = cleaned_data.get('email')
    password = cleaned_data.get('password')
    password_confirm = cleaned_data.get('password_confirm')
    #lets check if the passwords match
    if password and password_confirm and email and  (password != password_confirm) and (email != email):
      raise forms.ValidationError('Passwords do not match! Please enter correct password.')
    return cleaned_data
