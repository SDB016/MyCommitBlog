from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .models import Commit
from django.utils import timezone
import requests


def home(request):
    posts = Post.objects.all()
    return render(request, "home.html", {'posts': posts})

def posts(request):
    posts = Post.objects.all()
    return render(request, "posts.html", {'posts': posts})

def posting(request):
    if request.method == 'POST':
        token = request.POST['token']
        owner = request.POST['owner']
        repo = request.POST['repo']
        commits = getCommits(token, owner, repo)
        return render(request, "posting.html",{'commits':commits, 'token':token, 'owner':owner, 'repo':repo})
    else:
        return render(request,"posting.html")

def post(request, id):
    post = get_object_or_404(Post, pk = id)
    return render(request, "post.html", {'post': post})

def createPost(request):
    newPost = Post().create(request.POST['title'], request.POST['comments'])

    token = request.POST['token']
    owner = request.POST['owner']
    repo = request.POST['repo']
    commits = getCommits(token, owner, repo)
    for commit in commits:
        c = Commit()
        c.fileName = commit['files']
        c.message = commit['message']
        c.patch = commit['patch']
        c.post_id = newPost.id
        c.save()
    newPost.save()

    return redirect('post', newPost.id)

def editPost(request, id):
    editPost = get_object_or_404(Post, pk = id)
    return render(request, "edit.html", {'post': editPost})

def updatePost(request,id):
    updatePost = Post.objects.get(id=id)
    updatePost.title = request.POST['title']
    updatePost.comment = request.POST['comments']
    updatePost.updatedDate = timezone.now()
    updatePost.save()
    return redirect('post', updatePost.id)

def deletePost(request, id):
    deletePost = Post.objects.get(id=id)
    deletePost.delete()
    return redirect('posts')


def getCommits(token, owner, repo):
    commits = []
    query_url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {
        "state": "open",
    }

    headers = {'Authorization': f'token {token}'}
    r = requests.get(query_url, headers=headers, params=params)
    datas = r.json()
    for data in datas:
        # commit
        files_r = requests.get(query_url + f"/{data['sha']}", headers=headers, params=params)
        files_datas = files_r.json()

        commit_dict = {}
        commit_dict['date'] = data['commit']['author']['date']
        commit_dict['message'] = data['commit']['message']
        commit_dict['url'] = data['html_url']
        commit_dict['files'] = ""
        for file in files_datas['files']:
            commit_dict['files'] += file['filename'] + "\n"

        commit_dict['patch'] = files_datas['files'][0]['patch']

        commits.append(commit_dict)

        break
    return commits