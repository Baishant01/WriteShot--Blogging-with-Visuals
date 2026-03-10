from django.urls import path
from .views import add_comment_view, toggle_like_view

urlpatterns = [
    path("post/<int:id>/comment/add/", add_comment_view, name="add_comment"),
    path("post/<int:id>/like/", toggle_like_view, name="toggle_like"),
]
