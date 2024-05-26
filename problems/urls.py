from django.urls import path
<<<<<<< HEAD
from . import views
from .views import ProblemDetailView

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', ProblemDetailView.as_view(), name='problem-detail'),
]
=======

urlpatterns = [
]
>>>>>>> eb2e0ae (PYT-21: Craeted problems app and problem models)
