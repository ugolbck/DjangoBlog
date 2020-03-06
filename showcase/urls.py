from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/<int:article_id>/', views.proj_single, name='projects'), #Change article_id to article_slug
    path('CV/', views.cvDisplay, name='cvDisplay')
]