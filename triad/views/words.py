from django.http import QueryDict
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from triad.models import Word, Type

def list_all_words(request):
    from itertools import groupby

    words = Word.objects.all().order_by("type", "-potency")

    grouped_words = []
    for key, group in groupby(words, lambda x: x.type.id):
        grouped_words.append(list(group))

    return render(request, 'words/partials/_list.html', {'words': grouped_words})

@require_http_methods(['GET'])
def words(request):
    return render(request, 'words/index.html')

@require_http_methods(['GET'])
def word_form(request, word_id=None):
    types = Type.objects.all()

    word = None
    if word_id is not None:
        word = Word.objects.get(pk=word_id)

    return render(request, 'words/partials/_form.html', {'word': word, 'types': types})

@require_http_methods(['GET', 'PUT', 'DELETE'])
def word_details(request, word_id):
    word = Word.objects.get(pk=word_id)

    if request.method == 'GET':
        return render(request, 'words/partials/_detail.html', {'word': word})

    elif request.method == 'DELETE':
        word.delete()
        return list_all_words(request)

    elif request.method == 'PUT':
        data = QueryDict(request.body)

        word.word = data.get("word")
        word.potency = data.get("potency")
        word.type_id = data.get("type")
        word.save()

        return render(request, 'words/partials/_detail.html', {'word': word})

@require_http_methods(['GET', 'POST'])
def word_list(request):
    if request.method == 'GET':
        return list_all_words(request)

    elif request.method == 'POST':
        Word.objects.create(
            word=request.POST.get('word'),
            potency=request.POST.get('potency'),
            type=Type.objects.get(pk=request.POST.get('type')),
        )
        return list_all_words(request)
