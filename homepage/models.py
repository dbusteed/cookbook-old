from django.db import models
from django.conf import settings
from account.models import User

class Recipe(models.Model):
    """
    Recipe model
    """

    name = models.TextField()
    ingredients = models.TextField()
    steps = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='recipes')
    link = models.URLField(null=True)
    image_link = models.URLField(null=True)
    notes = models.TextField(default='')
    owner = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='my_recipes')
    create_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    def image_url(self):

        if self.image_link != '':
            url = self.image_link
        else:
            url = settings.STATIC_URL + 'homepage/media/images/image_unavailable.jpg'

        return url

class Category(models.Model):
    """
    Category model
    """
    name = models.TextField()

    def __str__(self):
        return self.name