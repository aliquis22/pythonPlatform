from django.contrib import admin
from django.urls import path
import articles.views as views


urlpatterns = [
    path('', views.index, name='home'),
    path('article/create', views.create, name='create')
]