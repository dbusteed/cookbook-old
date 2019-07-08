from django.conf import settings
from django_mako_plus import view_function
from homepage.models import Recipe, Category
from account.models import User
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth.decorators import login_required

@view_function
@login_required(login_url='/account/login/')
def process_request(request):
  
    # for POST requests
    if(request.method == "POST"):
        form = AddRecipeForm(request.POST)
  
        if(form.is_valid()): # check their password
            form.commit(request) # the form processing needs the request object
            return HttpResponseRedirect('/homepage/add/')
  
    # for GET requests show the blank form
    else:
        form = AddRecipeForm()
  
    context = {
        'form': form
    }

    return request.dmp.render('add.html', context)

class AddRecipeForm(forms.Form):
    name = forms.CharField(label='Recipe Title', required=True)
    ingredients = forms.CharField(label="Ingredients",widget=forms.Textarea(attrs={'rows': 3}), required=True)
    steps = forms.CharField(label="Steps",widget=forms.Textarea(attrs={'rows': 3}), required=True)
    category = forms.ModelChoiceField(label="Category", queryset=Category.objects.all(), empty_label=None)
    notes = forms.CharField(label="Notes", widget=forms.Textarea(attrs={'rows': 2}), required=False)
    link = forms.URLField(label='URL', required=False)
    image_link = forms.URLField(label='Image URL', required=False)
  
    def commit(self, req):
        r = Recipe()
        r.name = self.cleaned_data.get('name')
        r.ingredients = self.cleaned_data.get('ingredients')
        r.steps = self.cleaned_data.get('steps')
        r.category = self.cleaned_data.get('category')
        r.link = self.cleaned_data.get('link')
        r.notes = self.cleaned_data.get('notes')
        r.image_link = self.cleaned_data.get('image_link')
        r.owner = User.objects.get(id=req.user.id)
        r.save()