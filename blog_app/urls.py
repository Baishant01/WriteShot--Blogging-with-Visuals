from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list' ),
    path('post_details/<int:pk>/', views.post_details, name='post_details' ),
    path('post_create/', views.post_create, name='post_create' ),
    path('post_delete/<int:pk>', views.post_delete, name='post_delete' ),
]
