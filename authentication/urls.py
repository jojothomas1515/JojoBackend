from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from authentication import views
from authentication.views import MyTokenObtainPairView

urlpatterns = [
    # Your URLs...
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.signup_view, name='register')
]