from django.urls import path
from . import views

urlpatterns = [
    path('userinfo', views.userInfo, name='userInfo'),
    path('changepic', views.changeProfileImage, name="changepic"),
]