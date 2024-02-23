from django.urls import include, path
from .views import *


app_name = "triad"

urlpatterns = [
    path('', home, name='home'),
    path('potioningredients', ingredients, name='ingredients'),
    path('ingredients', ingredient_list, name='ingredient-list'),
    path('ingredients/<int:ingredient_id>', ingredient_details, name="ingredient"),
    path('ingredients/form', ingredient_form, name='ingredient_form'),
    path('ingredients/<int:ingredient_id>/form', ingredient_form, name='ingredient_form'),

    # path('logout', logout_user, name='logout'),
    # path('register', register_user, name='register'),
]
