from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from account.api import CustomTokenObtainPairView, ChangePasswordView, UserListAPI, GroupListAPI,\
    MarriedStatusAPI, ReligionAPI, RenterNidAPI, DashboardAPI
from account.views import ProfileAPI, ProfileFamilyMember, ProfileEmergencyContact, ProfileOtherMember, Registration

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/list/', UserListAPI.as_view()),
    path('group/list/', GroupListAPI.as_view()),
    path('married/list/', MarriedStatusAPI.as_view()),
    path('religion/list/', ReligionAPI.as_view()),
    path('change_password/<str:pk>/', ChangePasswordView.as_view()),
    path('registration/', Registration.as_view(), name="registration"),  # both for owner & renter
    path('profile/', ProfileAPI.as_view()),
    path('profile/update/', ProfileAPI.as_view()),

    path('profile/family/member/create/', ProfileFamilyMember.as_view()),
    path('profile/family/member/update/', ProfileFamilyMember.as_view()),
    path('profile/family/member/list/', ProfileFamilyMember.as_view()),
    path('profile/family/member/delete/', ProfileFamilyMember.as_view()),

    path('profile/emergency/contact/create/', ProfileEmergencyContact.as_view()),
    path('profile/emergency/contact/update/', ProfileEmergencyContact.as_view()),
    path('profile/emergency/contact/list/', ProfileEmergencyContact.as_view()),
    path('profile/emergency/contact/delete/', ProfileEmergencyContact.as_view()),

    path('profile/other/member/create/', ProfileOtherMember.as_view()),
    path('profile/other/member/update/', ProfileOtherMember.as_view()),
    path('profile/other/member/list/', ProfileOtherMember.as_view()),
    path('profile/other/member/delete/', ProfileOtherMember.as_view()),

    path('renter/nid/list/', RenterNidAPI.as_view()),
    path('dashboard/', DashboardAPI.as_view())

]
