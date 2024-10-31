from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'instructions', 'ingredients', 'image', 'image_alt', 'meal_type', 'cuisine_types', 'calories']
        widgets = {
            'instructions': CKEditor5Widget(config_name='extends'),  # Set to the name of your CKEditor configuration
            'ingredients': CKEditor5Widget(config_name='extends'),
        }
