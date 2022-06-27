from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('myposts', views.userPosts , name='myposts')
]