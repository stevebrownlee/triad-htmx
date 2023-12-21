from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from triad.models import Ingredient, Type

@require_http_methods(['GET'])
def ingredients(request):
    return render(request, 'ingredients/index.html')

@require_http_methods(['GET'])
def ingredient_form(request):
    types = Type.objects.all()
    return render(request, 'ingredients/partials/_form.html', {'ingredient': None, 'types': types})

@require_http_methods(['GET'])
def ingredient_details(request, ingredient_id):
    ingredient= Ingredient.objects.get(pk=ingredient_id)
    return render(request, 'ingredients/partials/_detail.html', {'ingredient': ingredient})


@require_http_methods(['GET', 'POST'])
def ingredient_list(request):
    if request.method == 'GET':
        ingredients = Ingredient.objects.all()
        return render(request, 'ingredients/partials/_list.html', {'ingredients': ingredients})

    elif request.method == 'POST':
        Ingredient.objects.create(
            name=request.POST.get('name'),
            potency=request.POST.get('potency'),
            type=Type.objects.get(pk=request.POST.get('type')),
        )
        ingredients = Ingredient.objects.all()
        return render(request, 'ingredients/partials/_list.html', {'ingredients': ingredients})


