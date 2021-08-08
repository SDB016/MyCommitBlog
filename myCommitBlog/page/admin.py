from django.contrib import admin
from .models import Post
from .models import Commit

admin.site.register(Post)
admin.site.register(Commit)