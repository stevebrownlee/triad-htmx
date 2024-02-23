from django.urls import include, path
from .views import *


app_name = "triad"

urlpatterns = [
    path('', home, name='home'),
    path('potioningredients', ingredients, name='ingredients'),
    path('ingredients', ingredient_list, name='ingredient-list'),
    path('ingredients/<int:ingredient_id>', ingredient_details, name="ingredient"),
    path('ingredients/form', ingredient_form, name='new-ingredient-form'),
    path('ingredients/<int:ingredient_id>/form', ingredient_form, name='edit-ingredient-form'),

    path('spellwords', words, name='words'),
    path('words', word_list, name='word-list'),
    path('words/<int:word_id>', word_details, name="word"),
    path('words/form', word_form, name='new-word-form'),
    path('words/<int:word_id>/form', word_form, name='edit-word-form'),

    # path('logout', logout_user, name='logout'),
    # path('register', register_user, name='register'),
]
