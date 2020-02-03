from django.shortcuts import render
from django.http import HttpResponse

from .models import Article

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, article_id):
    return HttpResponse("You're looking at article %s." % article_id)