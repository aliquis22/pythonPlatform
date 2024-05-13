from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)
    gender = models.BooleanField(default=True)
    birth_date = models.DateField(null=True, blank=True)
    objects = models.Manager()
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.photo:
            img = Image.open(self.photo.path)

            # Resize image
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(self.photo.path)
