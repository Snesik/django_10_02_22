from django.shortcuts import render
from django.http import HttpResponse

from .models import News


def index(requests):
    news = News.objects.all()
    return render(requests, 'news/index.html', {'news': news, 'title': 'Список новостей'})
