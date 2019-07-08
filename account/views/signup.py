from django import forms
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.http import HttpResponseRedirect
from account.models import User
from django_mako_plus import view_function
from datetime import datetime

@view_function
def process_request(request):
  
    # for POST requests
    if(request.method == "POST"):
        form = SignupForm(request.POST)
  
        if(form.is_valid()):
            form.commit(request)
            return HttpResponseRedirect('/index')
  
    # for GET requests show the blank form
    else:
        form = SignupForm()
  
    context = {
        'form': form
    }

    return request.dmp.render('signup.html', context)

class SignupForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'autofocus': 'autofocus'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput()) # the widget hides the password
    password2 = forms.CharField(label="Re-enter password", widget=forms.PasswordInput()) # the widget hides the password
    code = forms.CharField(label="Sign-up Code")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = User.objects.filter(email=email)
        if len(user) > 0:
            raise forms.ValidationError('The email address is already in use.')
        return email            

    # this is called in is_valid()
    def clean(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('Passwords must match.')

        if self.cleaned_data.get('code').lower() != datetime.now().strftime('%B').lower():
            raise forms.ValidationError('Incorrect sign-up code! Check your spelling? (it\'s not case sensitive)')

        return self.cleaned_data

    def commit(self, req):
        u = User()
        u.email = self.cleaned_data.get('email')
        u.set_password(self.cleaned_data.get('password'))
        u.save()

        user = authenticate(username = u.email, password = self.cleaned_data.get('password'))

        login(req, user)