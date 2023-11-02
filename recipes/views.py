from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def my_view(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Ícaro Gonçalves'
    })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Ícaro Gonçalves'
    })
