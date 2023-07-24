from django.shortcuts import render
from . import forms

# Create your views here.

def regform(request):
    form = forms.SignUp()
    if request.method == 'POST':
        form = forms.SignUp(request.POST)
        # message = 'You registed successfully. Thank you!'\
        if form.is_valid():
            message = 'Thank you!'
        else:
            message= 'Data is invalid, try again!'
    else:
        message = 'Input your information to register!'
    return render(request, 'signup.html', {'message': message, 'form' : form})
