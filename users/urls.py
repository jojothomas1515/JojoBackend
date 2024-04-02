from django.urls import path

from . import views

urlpatterns = [
    path('profile', views.userInfo, name='userInfo'),
    path('update-profile-pic', views.changeProfileImage, name="changepic"),
    path('profile/<str:username>', views.users_profile_view, name='usersprofile'),
]
