from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from owner.models import User, Owner, Unit
from django.contrib.auth.models import Group

from renter.models import CheckIn, Renter
from renter.serializers import CheckInSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import QueryDict


def check_in_list(queryset):
    serializer = CheckInSerializer(queryset, many=True)
    list_ = list()
    for unit_dict in serializer.data:
        unit_dict_ = dict(unit_dict)
        query_dict = QueryDict(mutable=True)
        query_dict['id'] = unit_dict_['id']
        query_dict['name'] = unit_dict_['name']
        query_dict['remark'] = unit_dict_['remark']
        query_dict['check_in'] = unit_dict_['check_in']
        query_dict['check_in_date'] = unit_dict_['check_in_date']
        query_dict['check_in_renter'] = unit_dict_['check_in_renter']
        if unit_dict_['check_in_renter']:
            query_dict['check_in_renter_name'] = [renter.user.username for renter in
                                                  Owner.objects.filter(id=unit_dict_['check_in_renter'])]
        else:
            query_dict['check_in_renter_name'] = 'None'

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
        user = self.get_object(request.user.pk)
        user_type = [group.name for group in Group.objects.filter(user=user)]

        if str(user_type[0]) == 'Owner':
            owner = Owner.objects.get(user=user)
            queryset = Unit.objects.filter(units=owner)
            list_ = check_in_list(queryset)
            return Response(list_, status=status.HTTP_200_OK)
        elif str(user_type[0]) == 'Renter':
            queryset = Unit.objects.filter(status=True)
            list_ = check_in_list(queryset)
            return Response(list_, status=status.HTTP_200_OK)

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

        return Response({'success': True}, status=status.HTTP_200_OK)

    def put(self, request, format=None):
        queryset = Unit.objects.get(id=request.data['id'])
        serializer = CheckInSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response({'success': True}, status=status.HTTP_200_OK)
