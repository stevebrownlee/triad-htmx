from django.http import QueryDict
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from triad.models import Ingredient, Type

def list_all_ingredients(request):
    from itertools import groupby

    ingredients = Ingredient.objects.all().order_by("type", "-potency")

    grouped_ingredients = []
    for key, group in groupby(ingredients, lambda x: x.type.id):
        grouped_ingredients.append(list(group))

    return render(request, 'ingredients/partials/_list.html', {'ingredients': grouped_ingredients})

@require_http_methods(['GET'])
def ingredients(request):
    return render(request, 'ingredients/index.html')

@require_http_methods(['GET'])
def ingredient_form(request, ingredient_id=None):
    types = Type.objects.all()

    ingredient = None
    if ingredient_id is not None:
        ingredient = Ingredient.objects.get(pk=ingredient_id)

    return render(request, 'ingredients/partials/_form.html', {'ingredient': ingredient, 'types': types})

@require_http_methods(['GET', 'PUT', 'DELETE'])
def ingredient_details(request, ingredient_id):
    ingredient = Ingredient.objects.get(pk=ingredient_id)

    if request.method == 'GET':
        return render(request, 'ingredients/partials/_detail.html', {'ingredient': ingredient})

    elif request.method == 'DELETE':
        ingredient.delete()
        return list_all_ingredients(request)

    elif request.method == 'PUT':
        data = QueryDict(request.body)

        ingredient.name = data.get("name")
        ingredient.potency = data.get("potency")
        ingredient.type_id = data.get("type")
        ingredient.save()

        return render(request, 'ingredients/partials/_detail.html', {'ingredient': ingredient})

@require_http_methods(['GET', 'POST'])
def ingredient_list(request):
    if request.method == 'GET':
        return list_all_ingredients(request)

    elif request.method == 'POST':
        Ingredient.objects.create(
            name=request.POST.get('name'),
            potency=request.POST.get('potency'),
            type=Type.objects.get(pk=request.POST.get('type')),
        )
        return list_all_ingredients(request)
