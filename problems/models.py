from django.db import models
from django.contrib.auth.models import User


class Problem(models.Model):
    DIFFICULTIES_CHOICES = [
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    ]

    problem_id = models.AutoField("ID", primary_key=True)
    title = models.CharField("Title", max_length=128)
    content = models.TextField("Content")
    difficulties = models.CharField(
        max_length=6,
        choices=DIFFICULTIES_CHOICES,
        default="easy",
    )

    def __str__(self):
        return '%s' % self.title


class Test(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.PROTECT)
    test_id = models.AutoField("ID", primary_key=True)
    input = models.CharField("Input", max_length=255)
    output = models.CharField("Output", max_length=255)


class Code(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    code_id = models.AutoField("ID", primary_key=True)
    content = models.TextField("content")
