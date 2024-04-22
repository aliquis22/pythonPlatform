from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
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
            return redirect('home')
    else:
        form = ArticleForm()
    data = {'form': form}
    return render(request, 'articles/create.html', data)


