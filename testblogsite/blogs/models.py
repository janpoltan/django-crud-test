from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(User, related_name='author')
    
    def __str__(self):
        return self.title

class ArticleTag(models.Model):
    name = models.CharField(max_length=25)
    articles = models.ManyToManyField(Article, related_name='tags')
    
    def __str__(self):
        return self.name

class Comment(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField()
    article = models.ForeignKey(Article, related_name='article')

    def __str__(self):
        return self.name
