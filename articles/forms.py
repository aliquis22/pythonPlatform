from .models import Article
from django.forms import ModelForm, Textarea, TextInput, FileInput

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'announce', 'text', 'image']
        widgets = {
            "title": TextInput(attrs={'class':'form-control', 'placeholder': 'Введите название статьи'}),
            "announce": Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите анонс статьи'}),
            "text": Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите текст статьи', 'style': 'width: 100%; height: 200px;'}),
            "image": FileInput(attrs={'class': 'form-control', 'placeholder': 'Выберите изображение'})
        }
