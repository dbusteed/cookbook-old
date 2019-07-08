from django.conf import settings
from django_mako_plus import view_function
from homepage.models import Recipe
from django import forms
from django.http import HttpResponseRedirect

@view_function
def process_request(request, recipe:Recipe):
    
    recipe.steps = recipe.steps.split('\n')
    recipe.ingredients = recipe.ingredients.split('\n')
    
    under_dir = ''

    if len(recipe.notes) != 0:
        recipe.notes = recipe.notes.split('\n')
        
        print(len(recipe.steps))
        print(len(recipe.ingredients))
        
        under_dir = 'True' if len(recipe.ingredients) >= len(recipe.steps) else 'False'

        print(under_dir)

    context = {
        'recipe': recipe,   
        'under_dir': under_dir,

    }
    return request.dmp.render('recipe.html', context)