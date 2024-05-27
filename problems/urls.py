from django.urls import path
from . import views
from .views import ProblemDetailView

app_name = 'problems'

urlpatterns = [
    path('', views.index, name='list'),
    path('<int:pk>/', ProblemDetailView.as_view(), name='problem-detail'),
]