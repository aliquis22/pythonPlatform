from django.contrib import admin
from django.urls import path
import roadmaps.views as views


urlpatterns = [
    path('', views.roadmap, name='roadmap'),
]