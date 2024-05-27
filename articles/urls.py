from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='home'),  # URL-маршрут для главной страницы
    path('article/create', views.create, name='create'),
    path('<int:id>/<slug:slug>', views.article_detail, name='article_detail'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]
