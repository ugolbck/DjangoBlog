from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.project_list, name='projects'),
    path('projects/<int:article_id>/', views.project_render, name='project_detail'),
    path('CV/', views.cvDisplay, name='cvDisplay')
]