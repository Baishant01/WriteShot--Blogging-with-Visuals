from django.db import models
from django.contrib.auth.models import User
from blog_app.models import Post

# Create your models here.


class Like(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        # To allow post.likes.all()
        related_name="likes",
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        # Allows user.blog_likes.all()
        related_name="blog_likes",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        # Prevention of duplicate likes

        unique_together = ["post", "user"]
        ordering = ["-created_at"]

    def __str__(self):
        return f"Liked by {self.user} on {self.post}."


class Comment(models.Model):

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        # allows post.comments.all()
        related_name="comments",
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        # allows user.blog_comments.all()
        related_name="blog_comments",
    )

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Comment by {self.user} on {self.post}."
