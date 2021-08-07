from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50, null=False)
    writer = models.CharField(max_length=20, null=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class Commit(models.Model):
    fileName = models.CharField(max_length=50, null=False)
    hashcode = models.CharField(max_length=10)
    url = models.URLField()
    message = models.TextField()
    comment = models.TextField()
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='포스트'
    )

    def __str__(self):
        return f'{self.post.title} {self.hashcode}'
