from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('my_posts/', views.user_post, name='myposts'),
    path('<str:username>/posts/', views.user_profile_post, name='myposts'),
    path('add_post/', views.add_post, name='addpost'),
    path('remove_post/<int:pk>/', views.remove_post, name='removepost'),
    path('view_post/<int:pk>/', views.view_post, name='viewpost'),
]
