from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from comments.forms import CommentForm
from django.utils import timezone


# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles':articles})


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
    return render(request, 'articles/article_detail.html', {'article': article, 'form': form, 'comments': comments})
