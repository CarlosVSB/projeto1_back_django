# from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_list_or_404

from recipes.models import Recipe
from utils.recipes.factory import make_recipe


def home(req):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(req, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(req, category_id):
    # recipes = Recipe.objects.filter(
    #     category__id=category_id,
    #     is_published=True
    # ).order_by('-id')

    # if not recipes:
    #     raise Http404('Not found 😓')
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True
        ).order_by('-id')
    )

    return render(req, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category |',
    })


def recipe(req, id):
    return render(req, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
