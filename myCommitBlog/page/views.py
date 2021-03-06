from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .models import Commit
from .models import File
from django.utils import timezone
import requests


def home(request):
    posts = Post.objects.all()
    sortedPosts = Post.objects.all().order_by('-hits')[:3]
    return render(request, "home.html", {'posts': posts, 'sortedPosts':sortedPosts})

def posts(request):
    posts = Post.objects.all()
    return render(request, "posts.html", {'posts': posts})

def posting(request):
    if request.method == 'POST':
        token = request.user.token
        owner = request.POST['owner']
        repo = request.POST['repo']
        commits = getCommits(token, owner, repo)
        return render(request, "posting.html",{'commits':commits, 'token':token, 'owner':owner, 'repo':repo})
    else:
        return render(request,"posting.html")

def post(request, id):
    post = get_object_or_404(Post, pk = id)
    post.click()
    return render(request, "post.html", {'post': post})

def createPost(request):
    comment_count = 0
    comments = request.POST.getlist('comments[]')
    newPost = Post().create(request.POST['title'])
    newPost.user = request.user
    token = request.user.token
    owner = request.POST['owner']
    repo = request.POST['repo']
    commits = getCommits(token, owner, repo)
    for commit in commits:
        c = Commit().create(newPost.id)
        c.comment = comments[comment_count]
        c.message = commit['message']
        for file in commit['files']:
            f = File()
            f.fileName = file['filename']
            f.patch = file['patch']
            f.commit_id = c.id
            f.save()
        c.save()
        comment_count +=1
    newPost.save()

    return redirect('post', newPost.id)

def editPost(request, id):
    editPost = get_object_or_404(Post, pk = id)
    return render(request, "edit.html", {'post': editPost})

def updatePost(request,id):
    updatePost = Post.objects.get(id=id)
    comment_count = 0
    comments = request.POST.getlist('comments[]')
    updatePost.title = request.POST['title']
    updatePost.updatedDate = timezone.now()
    updatePost.save()
    commits = Commit.objects.filter(post_id=id)
    for commit in commits:
        commit.comment = comments[comment_count]
        comment_count+=1
        commit.save()
    
    return render(request, "post.html", {'post': updatePost})

def deletePost(request, id):
    deletePost = Post.objects.get(id=id)
    deletePost.delete()
    return redirect('posts')


def getCommits(token, owner, repo):
    commit_count = 0
    file_count =0
    max_commit_num = 4
    max_file_num = 2
    commits = []
    query_url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {
        "state": "open",
    }

    headers = {'Authorization': f'token {token}'}
    r = requests.get(query_url, headers=headers, params=params)
    datas = r.json()
    for data in datas:
        if commit_count < max_commit_num:
            # commit
            files_r = requests.get(query_url + f"/{data['sha']}", headers=headers, params=params)
            files_datas = files_r.json()
            commit_dict = {}
            commit_dict['date'] = data['commit']['author']['date']
            commit_dict['message'] = data['commit']['message']
            commit_dict['url'] = data['html_url']
            commit_dict['files'] = []
            file_count = 0
            for file in files_datas['files']:
                if file_count < max_file_num:
                    file_dict = {}
                    file_dict['filename'] = file['filename']
                    file_dict['patch'] = file.get('patch')
                    commit_dict['files'].append(file_dict)
                    file_count +=1
            commits.append(commit_dict)
            commit_count +=1
        
        
    return commits


    