from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, "home.html", {'posts': posts})


def posts(request):
    posts = Post.objects.all()
    return render(request, "posts.html", {'posts': posts})


def posting(request):
    return render(request, "posting.html")

def post(request, id):
    post = get_object_or_404(Post, pk = id)
    return render(request, "post.html", {'post': post})



