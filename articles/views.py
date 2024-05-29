from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, ArticleViews
from comments.models import Comment
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from comments.forms import CommentForm
from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models import Count


# Create your views here.
def index(request):
    articles = Article.objects.all()
    most_viewed_articles = Article.objects.annotate(views_count=Count('articleviews')).order_by(
        '-articleviews__views_count')[:5]
    return render(request, 'index.html', {'articles': articles, 'most_viewed_articles': most_viewed_articles})


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('articles:home')
    else:
        form = ArticleForm()
    data = {'form': form}
    return render(request, 'articles/create.html', data)


def article_detail(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    article_views, created = ArticleViews.objects.get_or_create(article=article)
    if request.user.is_authenticated and request.user not in article_views.viewed_by_users.all():
        article_views.views_count += 1
        article_views.viewed_by_users.add(request.user)
        article_views.save()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.created_date = timezone.now()
            comment.save()
            return redirect('articles:article_detail', id=article.id, slug=article.slug)
    else:
        form = CommentForm()
    comments = article.comments.all()
    # Обработка редактирования комментария
    if 'edit_comment' in request.POST:
        comment_id = request.POST.get('comment_id')
        comment = get_object_or_404(Comment, id=comment_id, author=request.user)
        comment.text = request.POST.get('text')
        comment.updated_date = timezone.now()
        comment.save()
        return redirect('articles:article_detail', id=article.id, slug=article.slug)

    # Обработка удаления комментария
    if 'delete_comment' in request.POST:
        comment_id = request.POST.get('comment_id')
        comment = get_object_or_404(Comment, id=comment_id, author=request.user)
        comment.delete()
        return redirect('articles:article_detail', id=article.id, slug=article.slug)
    return render(request, 'articles/article_detail.html',
                  {'article': article, 'form': form, 'comments': comments, 'article_views': article_views})


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.updated_date = timezone.now()
            comment.save()
            return redirect('articles:article_detail', id=comment.article.id, slug=comment.article.slug)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'articles/article_detail.html', {'form': form, 'comment': comment})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    article_id = comment.article.id
    article_slug = comment.article.slug
    comment.delete()
    return redirect('articles:article_detail', id=article_id, slug=article_slug)
