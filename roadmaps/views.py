from django.shortcuts import render

from roadmaps.models import Chapter, Topic


# Create your views here.

def roadmap(request):
    chapters = Chapter.objects.all()
    topics = Topic.objects.all()
    return render(request, 'roadmaps/index.html',
                  {'chapters':chapters, 'topics':topics})