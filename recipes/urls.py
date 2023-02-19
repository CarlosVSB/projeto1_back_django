from django.urls import path

from recipes.views import contato, home, sobre

urlpatterns = [
    path('contato/', contato),
    path('sobre/', sobre),
    path('', home),
]
