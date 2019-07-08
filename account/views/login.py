from django import forms
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.http import HttpResponseRedirect
from account.models import *
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone

@view_function
def process_request(request):
  
    # for POST requests
    if(request.method == "POST"):
        form = LoginForm(request.POST)
  
        if(form.is_valid()): # check their password
            form.commit(request) # the form processing needs the request object
            return HttpResponseRedirect('/homepage/index')
  
    # for GET requests show the blank form
    else:
        form = LoginForm()
  
    context = {
        'form': form
    }

    return request.dmp.render('login.html', context)


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'autofocus': 'autofocus'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput()) # the widget hides the password
  
    # this is called in is_valid()
    def clean(self): 
        self.user = authenticate(email = self.cleaned_data.get('email'), password = self.cleaned_data.get('password'))
        if(self.user is None): # raise an error if the user wasn't authenticated
            raise forms.ValidationError('Unable to sign in. Invalid email/password.')
        return self.cleaned_data

    # log the user in
    def commit(self, request):
        login(request, self.user)