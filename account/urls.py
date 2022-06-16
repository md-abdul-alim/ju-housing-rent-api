from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from account.api import CustomTokenObtainPairView, ChangePasswordView, UserListAPI, RegisterView, GroupListAPI

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/list/', UserListAPI.as_view()),
    path('group/list/', GroupListAPI.as_view()),
    path('change_password/<str:pk>/', ChangePasswordView.as_view()),
    path('registration/', RegisterView.as_view(), name="register"),
]