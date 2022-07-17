from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from owner.models import User, Owner, Unit
from django.contrib.auth.models import Group

from renter.models import CheckIn, Renter
from renter.serializers import CheckInSerializer, RenterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import QueryDict


def check_in_list(queryset):
    serializer = RenterSerializer(queryset, many=True)
    list_ = list()
    for unit_dict in serializer.data:
        unit_dict_ = dict(unit_dict)
        query_dict = QueryDict(mutable=True)
        query_dict['id'] = unit_dict_['id']
        query_dict['renter_name'] = unit_dict_['user']['get_full_name']
        query_dict['renter_email'] = unit_dict_['user']['email']
        query_dict['renter_phone'] = unit_dict_['user']['phone']
        if unit_dict_['present_house_owner']:
            for user in User.objects.filter(id=unit_dict_['present_house_owner']):
                query_dict['present_house_owner_name'] = user.first_name + ' ' + user.last_name
                query_dict['present_house_owner_email'] = user.email
                query_dict['present_house_owner_phone'] = user.phone

            for unit in Unit.objects.filter(check_in_renter__id=unit_dict_['id']):
                query_dict['check_in_date'] = unit.check_in

        else:
            query_dict['present_house_owner_email'] = 'None'

        query_dict['check_in_admin_approve'] = unit_dict_['check_in_admin_approve']

        list_.append(query_dict)
    return list_


class CheckInAPI(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, ]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request):
        queryset = Renter.objects.filter(previous_house_owner__isnull=True,
                                         present_house_owner__isnull=False, check_in_admin_approve=False)
        serializer = check_in_list(queryset)
        return Response(serializer, status=status.HTTP_200_OK)
        # user = self.get_object(request.user.pk)
        # user_type = [group.name for group in Group.objects.filter(user=user)]
        #
        # if str(user_type[0]) == 'Owner':
        #     owner = Owner.objects.get(user=user)
        #     queryset = Unit.objects.filter(units=owner)
        #     list_ = check_in_list(queryset)
        #     return Response(list_, status=status.HTTP_200_OK)
        # elif str(user_type[0]) == 'Admin':
        #     queryset = Unit.objects.filter(status=True)
        #     list_ = check_in_list(queryset)
        #     return Response(list_, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        user = self.get_object(request.user.pk)
        renter = Renter.objects.get(user=user)
        check_in_date = request.data["to_let_from"]
        remark = request.data["remark"]
        unit_code = request.data["code"]

        if not CheckIn.objects.filter(unit_code=unit_code, status=False).exists():
            CheckIn.objects.create(renter=renter, unit_code=unit_code, check_in_date=check_in_date, remark=remark)

            if Unit.objects.filter(check_in_renter=renter).exists():

                unit_checkout = Unit.objects.get(check_in_renter=renter)
                unit_checkout.check_out_date = check_in_date
                unit_checkout.check_out_renter = renter
                unit_checkout.check_out_status = True
                unit_checkout.save()

            if Unit.objects.filter(code=unit_code).exists():
                unit_checkin = Unit.objects.get(code=unit_code)

                if int(unit_checkin.check_in_permission_nid) == int(renter.user.nid):
                    unit_checkin.check_in_status = True
                    unit_checkin.status = False
                    unit_checkin.save()

            if renter.check_out_admin_approve and renter.check_in_admin_approve:
                renter.check_in_admin_approve = False
                renter.check_out_admin_approve = False
                renter.save()

        return Response({'success': True}, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        queryset = Renter.objects.get(id=id)
        queryset.check_in_admin_approve = True
        queryset.save()

        return Response({'success': True}, status=status.HTTP_200_OK)


def check_out_list(queryset):
    serializer = RenterSerializer(queryset, many=True)
    list_ = list()
    for unit_dict in serializer.data:
        unit_dict_ = dict(unit_dict)
        query_dict = QueryDict(mutable=True)
        query_dict['id'] = unit_dict_['id']
        query_dict['renter_name'] = unit_dict_['user']['get_full_name']
        query_dict['renter_email'] = unit_dict_['user']['email']
        query_dict['renter_phone'] = unit_dict_['user']['phone']
        if unit_dict_['previous_house_owner']:
            for user in User.objects.filter(id=unit_dict_['previous_house_owner']):
                query_dict['previous_house_owner_name'] = user.first_name + ' ' + user.last_name
                query_dict['previous_house_owner_email'] = user.email
                query_dict['previous_house_owner_phone'] = user.phone

            for unit in Unit.objects.filter(check_out_renter__id=unit_dict_['id']):
                query_dict['check_out_date'] = unit.check_out

        else:
            query_dict['previous_house_owner_email'] = 'None'

        query_dict['rent_of_date'] = unit_dict_['rent_of_date']
        query_dict['check_out_admin_approve'] = unit_dict_['check_out_admin_approve']

        list_.append(query_dict)
    return list_


class CheckOutAPI(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, ]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request):
        queryset = Renter.objects.filter(previous_house_owner__isnull=False,
                                         present_house_owner__isnull=True, check_out_admin_approve=False)
        serializer = check_out_list(queryset)
        return Response(serializer, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        check_out_date = request.data["check_out_date"]
        renter = Renter.objects.get(user__pk=request.user.pk)
        if Unit.objects.filter(check_in_renter=renter).exists():
            unit_checkout = Unit.objects.get(check_in_renter=renter)
            if not unit_checkout.check_out_status:
                unit_checkout.check_out_date = check_out_date
                unit_checkout.check_out_renter = renter
                unit_checkout.check_out_status = True
                unit_checkout.save()

                renter.previous_house_owner = renter.present_house_owner
                renter.present_house_owner = None
                renter.save()

        return Response({'success': True}, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        renter = Renter.objects.get(id=id)
        renter.check_out_admin_approve = True
        renter.previous_house_owner = None
        renter.save()

        return Response({'success': True}, status=status.HTTP_200_OK)

