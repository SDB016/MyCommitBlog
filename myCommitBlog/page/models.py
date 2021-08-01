from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50, null=False)
    content = models.TextField()
    writer = models.CharField(max_length=20, null=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]

