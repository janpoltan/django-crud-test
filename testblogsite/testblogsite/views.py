from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Article, ArticleTag, Comment

def landing(request):
    articles_total = Article.objects.count()
    tags_total = ArticleTag.objects.count()
    comments_total = Comment.objects.count()

    return render(request, 'landing.html', {
        'articles_total': articles_total,
        'tags_total': tags_total,
        'comments_total': comments_total 
    })

# List all articles
def home(request):
    articles = Article.objects.all()
    
    # Not the best way to attached related models
    # How do we automatically attached models or access them ?

    for article in articles:
        article.article_tags = ArticleTag.objects.filter(articles=article)
        article.article_comments = Comment.objects.filter(article=article)
        # article.tags return None even with tags assigned, why? Need to check models setup

    return render(request, 'list_articles.html', 
        {
            'articles': articles,
        }
    )   

# View a single article
def article(request, articleId):
    article = Article.objects.get(pk=articleId)
    article.article_tags = ArticleTag.objects.filter(articles=article)
    article.article_comments = Comment.objects.filter(article=article)

    return render(request, 'view_article.html', { 'article' : article })

# List all article by tags
def tags(request, tag):
    return HttpResponse('Tag by %s' % tag)

# List all tags by user
def user(request, userId):
    return HttpResponse('User by %s' % userId)
