from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    author = forms.CharField(label='Ваше имя:', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите имя',
    }))
    text = forms.CharField(label='Комментарий:', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Введите комментарий',
    }))

    class Meta:
        model = Comment
        fields = ('author', 'text')
