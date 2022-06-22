from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from account.api import CustomTokenObtainPairView, ChangePasswordView, UserListAPI, GroupListAPI,\
    MarriedStatusAPI, ReligionAPI
from account.views import ProfileAPI, ProfileFamily

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/list/', UserListAPI.as_view()),
    path('group/list/', GroupListAPI.as_view()),
    path('married/status/list/', MarriedStatusAPI.as_view()),
    path('religion/list/', ReligionAPI.as_view()),
    path('change_password/<str:pk>/', ChangePasswordView.as_view()),
    path('registration/', ProfileAPI.as_view(), name="registration"),  # both for owner & renter
    path('profile/', ProfileAPI.as_view()),
    path('profile/update/', ProfileAPI.as_view()),
    path('profile/family/member/create/', ProfileFamily.as_view()),
    path('profile/family/member/update/', ProfileFamily.as_view()),
    path('profile/family/member/list/', ProfileFamily.as_view()),
    path('profile/family/member/delete/', ProfileFamily.as_view()),
    path('profile/emergency/contact/update/', ProfileAPI.as_view()),
    path('profile/emergency/contact/delete/', ProfileAPI.as_view()),
    path('profile/home/cleaner/update/', ProfileAPI.as_view()),
    path('profile/home/cleaner/delete/', ProfileAPI.as_view()),
    path('profile/home/driver/update/', ProfileAPI.as_view()),
    path('profile/home/driver/delete/', ProfileAPI.as_view()),
]