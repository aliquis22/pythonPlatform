from django import forms
from django.forms import Textarea, IntegerField
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']
        widgets = {
            "comment": Textarea(attrs={
                'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Введите текст комментарии', 'style': 'width: 100%; height: 200px;'}),
        }
