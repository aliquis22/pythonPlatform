from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='home'),  # URL-маршрут для главной страницы
    path('article/create', views.create, name='create'),
    # Другие URL-маршруты вашего приложения...
]
