from django.conf import settings
from django.contrib.auth import logout
from django_mako_plus import view_function
from django.http import HttpResponseRedirect

@view_function
def process_request(request):

    logout(request)

    return HttpResponseRedirect('/homepage/index')
