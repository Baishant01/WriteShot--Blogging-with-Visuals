from django import forms
from .models import Like, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

        widgets = {
            "content": forms.Textarea(
                attrs={
                    "rows": 3,
                    "style": "width: 100%; padding:10px;",
                    "placeholder": "Write a comment...",
                }
            )
        }
