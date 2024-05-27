from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from articles.models import Article

class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(null=True, blank=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def edit_text(self, new_text):
        self.text = new_text
        self.updated_date = timezone.now()
        self.save()

    def remove(self):
        self.delete()
    def __str__(self):
        return self.text

