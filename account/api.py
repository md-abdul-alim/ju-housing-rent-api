from account.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import Group

from account.serializers import (
    CustomTokenObtainPairSerializer,
    ChangePasswordSerializer,
    UserEmailSerializer,
    RegistrationSerializer,
    GroupSerializer
)
from rest_framework.generics import (
    UpdateAPIView,
    CreateAPIView,
    ListAPIView
)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ChangePasswordView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer


class UserListAPI(ListAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = User.objects.all()
    serializer_class = UserEmailSerializer


class GroupListAPI(ListAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

