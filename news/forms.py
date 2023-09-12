from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
# from django.forms import widgets


class ModDateTimeInput(DateTimeInput):
    input_type = "datetime-local"


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = {"title", "anons", "news_text", "date"}
        widgets = {
            'title': TextInput(attrs={
                "class": "form-control",
                "placeholder": "Название Статьи",
            }),
            'anons': TextInput(attrs={
                "class": "form-control",
                "placeholder": "Анонс Статьи",
            }),
            "date": ModDateTimeInput(attrs={
                "class": "form-control",
                "placeholder": "Дата Публикации",
            }),
            "news_text": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Текст Статьи",
            }),
        }
