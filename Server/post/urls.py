from django.contrib import admin
from django.urls import path
from . import views

app_name='post'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post_create/', views.post_create, name = 'post_create'),
    path('<int:post_pk>/comment_create/', views.comment_create, name='comment_create'),
    path('<int:post_pk>/like/', views.like, name='like'),
    path('<int:post_pk>/<int:comment_pk>/', views.comment_delete, name='comment_delete'),
]
