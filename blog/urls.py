from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('myposts', views.userPosts, name='myposts'),
    path('addpost', views.addPost, name='addpost'),
    path('removepost/<int:pk>', views.removePost, name='removepost'),
    path('viewpost/<int:pk>', views.viewPost, name='viewpost')
]
