from django import forms
from .models import Post

class CreatePostForm(forms.Form):
    title = forms.CharField(max_length=100, label="عنوان")
    author = forms.CharField(max_length=100, label="نویسنده")
    text = forms.CharField(label="متن")
    cover = forms.ImageField(label="عکس",)


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'text','cover']


