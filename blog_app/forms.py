from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ["created_at", "author"]
        labels = {"is_private": "Do you want your post private?"}
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter post title"}
            ),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "image": forms.FileInput(
                attrs={"class": "form-control", "accept": "image/*"}
            ),
        }
