from django.shortcuts import render
from django.http import HttpResponse
from .models import Problem
from django.views.generic import ListView, DetailView


def index(request):
    problems = Problem.objects.all()

    return render(request, 'problems/index.html', {'problems': problems})


class ProblemDetailView(DetailView):
    model = Problem
    template_name = 'problems/detail.html'
    context_object_name = 'problem'
