from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=50, null=False)
    #comment = models.TextField(null=True) #TODO comment필드를 commit 객체에 할당
    writer = models.CharField(max_length=20, null=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    def create(self, title):
        newPost = Post()
        newPost.title = title
        newPost.writer = "withCat"
        newPost.createdDate = timezone.now()
        newPost.updatedDate = timezone.now()
        newPost.save()
        return newPost

    def __str__(self):
        return self.title

class Commit(models.Model):
    comment = models.TextField(null=True)
    hashcode = models.CharField(max_length=10)
    url = models.URLField()
    message = models.TextField(null=False)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='포스트',
        related_name='commit'
    )
    def create(self,post_id):
        newCommit = Commit()
        newCommit.post_id = post_id
        newCommit.save()
        return newCommit

class File(models.Model):
    fileName = models.TextField()
    patch = models.TextField()
    commit = models.ForeignKey(
        Commit,
        on_delete=models.CASCADE,
        verbose_name='커밋',
        related_name='file'
    )