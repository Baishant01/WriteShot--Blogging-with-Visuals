from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list' ),
    path('post_details/<int:pk>/', views.post_details, name='post_details' ),
    path('post_form/', views.post_form, name='post_form' ),
]
