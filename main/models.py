from statistics import mode
from django.db import models
from django.conf import settings
# Create your models here.
class BlogPost(models.Model):
    title = models.TextField(default='title')
    content = models.TextField(default='content')
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    