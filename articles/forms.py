from .models import Article
from django.forms import ModelForm, Textarea, TextInput, FileInput


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'announce', 'text', 'image']
        widgets = {
            "title": TextInput(attrs={'class':'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5', 'placeholder': 'Введите название статьи'}),
            "announce": Textarea(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5', 'placeholder': 'Введите анонс статьи'}),
            "text": Textarea(attrs={'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500', 'placeholder': 'Введите текст статьи', 'style': 'width: 100%; height: 200px;'}),
            "image": FileInput(attrs={'class': 'form-control', 'placeholder': 'Выберите изображение'})
        }
