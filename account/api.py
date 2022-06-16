from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import Group

from account.serializers import (
    CustomTokenObtainPairSerializer,
    ChangePasswordSerializer,
    UserSerializer,
    RegisterSerializer,
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
    serializer_class = UserSerializer


class RegisterView(CreateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class GroupListAPI(ListAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

