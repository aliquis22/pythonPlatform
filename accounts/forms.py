from django import forms
from .models import UserProfile

class PhotoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['photo']
