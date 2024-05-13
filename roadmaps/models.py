from django.db import models
from django.contrib.auth.models import User

class Chapter(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Topic(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class UserCompletedTopic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.topic.title} - Completed"
