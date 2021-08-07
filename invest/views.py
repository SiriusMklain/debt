from django.shortcuts import render

from .models import InvestPost


def index(request):
    posts = InvestPost.objects.all()
    return render(request, 'invest/index.html', context={'posts': posts})
