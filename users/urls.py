from django.urls import path

from . import views

urlpatterns = [
    path('userinfo', views.userInfo, name='userInfo'),
    path('changepic', views.changeProfileImage, name="changepic"),
    path('changeinfo', views.changeName, name='changeinfo'),
    path('<str:username>/profile', views.users_profile_view, name='usersprofile'),
]
