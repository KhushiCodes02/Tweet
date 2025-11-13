from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.list_tweet, name='list_tweet'),
    path('create/', views.create_tweet, name='create_tweet'),
    path('<int:tweet_id>/edit/', views.edit_tweet, name='edit_tweet'),
    path('<int:tweet_id>/delete/', views.delete_tweet, name='delete_tweet'),
]