from account.models import User, MarriedStatus, Religion
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import Group
import datetime
from rest_framework.response import Response
from dateutil.relativedelta import relativedelta


from account.serializers import (
    CustomTokenObtainPairSerializer,
    ChangePasswordSerializer,
    UserEmailSerializer,
    RegistrationSerializer,
    GroupSerializer, MarriedStatusSerializer, ReligionSerializer, RenterNidSerializer
)
from rest_framework.generics import (
    UpdateAPIView,
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView
)

from owner.models import Unit


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


class MarriedStatusAPI(ListAPIView):
    permission_classes = []
    queryset = MarriedStatus.objects.all()
    serializer_class = MarriedStatusSerializer


class ReligionAPI(ListAPIView):
    permission_classes = []
    queryset = Religion.objects.all()
    serializer_class = ReligionSerializer


class RenterNidAPI(ListAPIView):
    permission_classes = []
    queryset = User.objects.filter(renter_status=True)
    serializer_class = RenterNidSerializer


class DashboardAPI(RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        total_house_owner = User.objects.filter(is_archived=False, owner_status=True).count()
        total_unit = Unit.objects.filter(is_archived=False).count()
        total_unregistered_renter = User.objects.filter(nid__isnull=True, is_archived=False, renter_status=True).count()
        total_registered_renter = User.objects.filter(nid__isnull=False, is_archived=False, renter_status=True).count()

        return Response(data={
            "total_house_owner": total_house_owner,
            "total_unit": total_unit,
            "total_unregistered_renter": total_unregistered_renter,
            "total_registered_renter": total_registered_renter,
        })
