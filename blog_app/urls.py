from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list' ),
    path('<int:pk>/<str:title>/post_details/', views.post_details, name='post_details' ),
    path('my_posts/', views.my_posts_view, name='my_post_list' ),
    path('post_create/', views.post_create, name='post_create' ),
    path('<int:pk>/<str:title>/post_edit/', views.post_edit, name='post_edit' ),
    path('<int:pk>/<str:title>/post_delete/', views.post_delete, name='post_delete' ),
]
