from django.urls import path
from . import views
from .views import ProblemDetailView

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', ProblemDetailView.as_view(), name='problem-detail'),
]
