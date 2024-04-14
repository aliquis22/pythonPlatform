from django.shortcuts import render
from django.http import HttpResponse
from .models import Problem


def index(request):
    problems = Problem.objects.all()

    return render(request, 'problems/index.html', {'problems': problems})
