"""myCommitBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from page import views as p

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', p.home, name='home'),
    path('posts/', p.posts, name='posts'),
    path('posting/', p.posting, name='posting'),
    path('<str:id>', p.post, name='post'),
    path('account/', include('account.urls')),
    path('createPost/', p.createPost, name='createPost'),
    path('edit/<str:id>', p.editPost, name='editPost'),
    path('update/<str:id>', p.updatePost, name='updatePost'),
    path('delete/<str:id>', p.deletePost, name='deletePost')

]
