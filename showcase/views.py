from django.shortcuts import render, get_object_or_404

from .models import Article, CV


def index(request):
    latest_articles = Article.objects.order_by('-date')[:3]
    return render(request, 'showcase/index.html', {'latest_articles': latest_articles})

def proj_all(request):
    all_articles = Article.objects.all()
    return render(request, 'showcase/detail.html', {'all_articles': all_articles})

def proj_single(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'showcase/detail.html', {'article': article.body})

def cvDisplay(request):
    cv = get_object_or_404(CV, pk=1)
    return render(request, 'showcase/cv.html', {'cv': cv.curriculum})