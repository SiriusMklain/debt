from django.shortcuts import render

from invest.models import InvestPost


def index(request):
    post = InvestPost.objects.all()
    return render(request, 'completion/index.html', context={'post': post})
