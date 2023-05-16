from django.shortcuts import render

from .forms import RegisterForm

# Create your views here.


def register_view(req):
    form = RegisterForm()
    return render(req, 'authors/pages/register_view.html', {
        'form': form
    })
