from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from authentication import views
from authentication.views import MyTokenObtainPairView, MyTokenRefreshView

urlpatterns = [
    # Your URLs...
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.signup_view, name='register')
]