from django.urls import path
from . import views
from .views import ProblemDetailView, run_code, save_code, check_code

app_name = 'problems'

urlpatterns = [
    path('', views.index, name='list'),
    path('<int:pk>/', ProblemDetailView.as_view(), name='problem-detail'),
    path('run_code/', run_code, name='run_code'),
    path('save_code/', save_code, name='save_code'),
    path('check_code/', check_code, name='check_code'),  # Добавленный URL для проверки кода
]
