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
    content = models.CharField("Content", max_length=255)
    difficulties = models.CharField(
        max_length=6,
        choices=DIFFICULTIES_CHOICES,
        default="easy",
    )

    def __str__(self):
        return '%s' % self.title


class Test(models.Model):
    test_id = models.AutoField("ID", primary_key=True)
    input = models.CharField("Input", max_length=255)
    output = models.CharField("Output", max_length=255)


class ProblemTest(models.Model):
    problem_test_id = models.AutoField("ID", primary_key=True)
    problem = models.ForeignKey(Problem, on_delete=models.PROTECT)
    test = models.ForeignKey(Test, on_delete=models.PROTECT)


class Code(models.Model):
    code_id = models.AutoField("ID", primary_key=True)
    content = models.CharField("content", max_length=255)


class ProblemCode(models.Model):
    problem_code_id = models.AutoField("ID", primary_key=True)
    problem = models.ForeignKey(Problem, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    code = models.ForeignKey(Code, on_delete=models.PROTECT)
