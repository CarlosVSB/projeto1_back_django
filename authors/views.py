from django.shortcuts import render

# Create your views here.


def register_view(req):
    return render(req, 'authors/pages/register_view.html')
