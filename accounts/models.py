from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Дополнительные поля профиля
    phone_number = models.CharField(max_length=20, blank=True)
    gender = models.BooleanField(default=True)
    birth_date = models.DateField(null=True, blank=True)  # true - м, false - ж
    objects = models.Manager()
