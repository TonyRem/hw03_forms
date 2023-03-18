from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'group']
        labels = {'text': 'Текст  поста', 'group': 'Группа'}
        help_texts = {
            'text': 'Текст поста',
            'group': 'Группа, к которой будет относиться пост (необязательно)',
        }
        widgets = {'text': forms.Textarea(attrs={'rows': 3})}
