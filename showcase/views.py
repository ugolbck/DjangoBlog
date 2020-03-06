from django.shortcuts import render, get_object_or_404

from .models import Article, CV


def index(request):
    latest_articles = Article.objects.order_by('-date')[:3]
    return render(request, 'showcase/index.html', {'latest_articles': latest_articles})

# TODO
# Add projects.html and display all articles
# Split project_render into single/all
# Map urls in base.html to the right names from urls.py

def project_render(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    all_articles = Article.objects.all()
    return render(request, 'showcase/detail.html', {'article': article, 'all_articles': all_articles})

def cvDisplay(request):
    cv = get_object_or_404(CV, pk=1)
    return render(request, 'showcase/cv.html', {'cv': cv.curriculum})