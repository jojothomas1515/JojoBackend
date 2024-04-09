from django.urls import path

from . import views

urlpatterns = [
    path('', views.userInfo, name='userInfo'),
    path('update_profile_pic/', views.changeProfileImage, name="changepic"),
    path('<str:username>/', views.users_profile_view, name='usersprofile'),
]
