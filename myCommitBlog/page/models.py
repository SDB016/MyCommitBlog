from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=50, null=False)
    comment = models.TextField(null=True) #TODO comment필드를 commit 객체에 할당
    writer = models.CharField(max_length=20, null=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    def create(self, title, comments):
        newPost = Post()
        newPost.title = title
        newPost.writer = "withCat"
        newPost.comment = comments
        newPost.createdDate = timezone.now()
        newPost.updatedDate = timezone.now()
        newPost.save()
        return newPost

    def __str__(self):
        return self.title

class Commit(models.Model):
    fileName = models.CharField(max_length=50)
    hashcode = models.CharField(max_length=10)
    url = models.URLField()
    message = models.TextField()
    patch = models.TextField()
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='포스트',
        related_name='commit'
    )

