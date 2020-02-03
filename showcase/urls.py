from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('CV/<int:cv_id>/', views.cvDisplay, name='cvDisplay')
]