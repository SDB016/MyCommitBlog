from django.urls import path
from .views import *

urlpatterns = [
    path('createPost/', createPost, name='createPost'),
    path('edit/<str:id>', editPost, name='editPost'),
    path('update/<str:id>', updatePost, name='updatePost'),
    path('delete/<str:id>', deletePost, name='deletePost'),
    path('', home, name='home'),
    path('posts/', posts, name='posts'),
    path('posting/', posting, name='posting'),
    path('<str:id>', post, name='post')
]