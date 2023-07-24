from django import forms
from django.core import validators

def check_size(value):
    if len(value)<6:
        raise forms.ValidationError("the Password is too short")
    
class SignUp(forms.Form):
    first_name = forms.CharField(initial= 'First Name')
    last_name = forms.CharField(required= False)
    email = forms.EmailField(help_text='Write your email',required=False)
    address = forms.CharField(required=False,)
    technology = forms.CharField(initial='Django', disabled= True,)
    age = forms.IntegerField(required=False,)
    password = forms.CharField(widget=forms.PasswordInput, validators= [check_size,])
    re_password = forms.CharField(required=False, widget=forms.PasswordInput)

    # def clean_password(self):
    #     password = self.cleaned_data['password']
    #     if len(password) < 4:
    #         raise forms.ValidationError("Password is too short~!")
    #     return password