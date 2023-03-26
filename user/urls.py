from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user.views import UserUpdateAPIView, UserCreateAPIView, UserListAPIView

urlpatterns = [
    path('user/update/<int:pk>/', UserUpdateAPIView.as_view()),
    path('user/create/', UserCreateAPIView.as_view()),
    path('user/list/', UserListAPIView.as_view()),

    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]
