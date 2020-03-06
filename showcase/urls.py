from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.proj_all, name='proj_all'),
    path('projects/<int:article_id>/', views.proj_single, name='proj_single'), #Change article_id to article_slug
    path('CV/', views.cvDisplay, name='cvDisplay')
]