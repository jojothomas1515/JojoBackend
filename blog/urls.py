from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('myposts', views.user_post, name='myposts'),
    path('<str:username>/profile/posts', views.user_profile_post, name='myposts'),
    path('addpost', views.add_post, name='addpost'),
    path('removepost/<int:pk>', views.remove_post, name='removepost'),
    path('viewpost/<int:pk>', views.view_post, name='viewpost'),
]
