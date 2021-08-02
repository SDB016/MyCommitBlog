from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, "home.html", {'posts': posts})


def posts(request):
    posts = Post.objects.all()
    return render(request, "posts.html", {'posts': posts})


def posting(request):
    return render(request, "posting.html")



