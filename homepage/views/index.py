from django.conf import settings
from django_mako_plus import view_function, jscontext
from homepage.models import Recipe, Category
from math import ceil

NUM_PER_PAGE = 20

@view_function
def process_request(request):

    recipes = Recipe.objects.all()

    cat_id = 0
    search, cat_name, my_rec = '', '', ''

    if request.method == 'POST':

        search = request.POST.get('search', None)
        cat_id = request.POST.get('cat_id', None)
        my_rec = request.POST.get('my_rec', None)

        if search:
            recipes = recipes.filter(name__iregex=search)

        if cat_id:
            recipes = recipes.filter(category_id=cat_id)
            cat_name = Category.objects.get(id=cat_id).name + ' '

        if my_rec:
            if my_rec == 'True':
                recipes = recipes.filter(owner=request.user)

    num_pages = ceil(recipes.count() / NUM_PER_PAGE)

    context = {
        jscontext('search'): search,
        jscontext('cat_id'): cat_id,
        jscontext('num_pages'): num_pages,
        jscontext('my_rec'): (my_rec == 'True'),
        'cat_name': cat_name,
    }

    return request.dmp.render('index.html', context)

@view_function
def recipes(request, page_num:int=1, my_rec:bool=False, search:str='', cat_id:int=0):

    recipes = Recipe.objects.all()

    if search != '':
        recipes = recipes.filter(name__iregex=search)

    if cat_id > 0:
        recipes = recipes.filter(category_id=cat_id)

    if my_rec:
        recipes = recipes.filter(owner=request.user)
        
    recipes = recipes.order_by('name')

    recipes = recipes[((page_num - 1) * NUM_PER_PAGE):(page_num * NUM_PER_PAGE)]

    is_recipes = True

    if(len(recipes) == 0):
        is_recipes = False

    context = {
        'recipes': recipes,
        'is_recipes': is_recipes,
    }

    return request.dmp.render('index.recipes.html', context)