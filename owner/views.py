from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from owner.models import User, Owner, Unit
from django.contrib.auth.models import Group
from owner.serializers import OwnerSerializer, UnitSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import QueryDict

from renter.models import Renter


def to_let_list(queryset):
    serializer = UnitSerializer(queryset, many=True)
    list_ = list()
    for unit_dict in serializer.data:
        unit_dict_ = dict(unit_dict)
        query_dict = QueryDict(mutable=True)
        query_dict['id'] = unit_dict_['id']
        query_dict['name'] = unit_dict_['name']
        query_dict['code'] = unit_dict_['code']
        query_dict['type'] = unit_dict_['type']
        query_dict['square_feet'] = unit_dict_['square_feet']
        query_dict['bedrooms'] = unit_dict_['bedrooms']
        query_dict['rent'] = unit_dict_['rent']
        query_dict['address'] = unit_dict_['address']
        query_dict['description'] = unit_dict_['description']
        query_dict['to_let_from'] = unit_dict_['to_let_from']
        query_dict['to_let_date'] = unit_dict_['to_let_date']
        query_dict['check_in'] = unit_dict_['check_in']
        query_dict['check_in_date'] = unit_dict_['check_in_date']
        query_dict['check_out'] = unit_dict_['check_out']
        query_dict['check_out_date'] = unit_dict_['check_out_date']
        query_dict['check_in_renter'] = unit_dict_['check_in_renter']
        query_dict['check_out_renter'] = unit_dict_['check_out_renter']
        query_dict['check_in_permission_nid'] = unit_dict_['check_in_permission_nid']
        if unit_dict_['check_in_renter']:
            query_dict['check_in_renter_name'] = [renter.user.username for renter in Renter.objects.filter(id=unit_dict_['check_in_renter'])]
        else:
            query_dict['check_in_renter_name'] = 'None'

        if unit_dict_['check_out_renter']:
            query_dict['check_out_renter_name'] = [renter.user.username for renter in
                                                  Renter.objects.filter(id=unit_dict_['check_out_renter'])]
        else:
            query_dict['check_out_renter_name'] = 'None'

        if unit_dict_['status']:
            query_dict['status'] = "True"
        else:
            query_dict['status'] = "False"
        list_.append(query_dict)
    return list_


class ToLet(APIView):
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
            list_ = to_let_list(queryset)
            return Response(list_, status=status.HTTP_200_OK)
        elif str(user_type[0]) == 'Renter':
            queryset = Unit.objects.filter(status=True)
            list_ = to_let_list(queryset)
            return Response(list_, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        user = self.get_object(request.user.pk)
        owner = Owner.objects.get(user=user)
        name = request.data["name"]
        type_ = request.data["type"]
        square_feet = request.data["square_feet"]
        bedrooms = request.data["bedrooms"]
        rent = request.data["rent"]
        address = request.data["address"]
        description = request.data["description"]
        to_let_from = request.data["to_let_from"]

        unit = Unit.objects.create(
            name=name,
            type=type_,
            square_feet=square_feet,
            bedrooms=bedrooms,
            rent=rent,
            address=address,
            description=description,
            to_let_from=to_let_from,
        )
        unit.save()
        owner.unit.add(unit)
        owner.save()

        return Response({'success': True}, status=status.HTTP_200_OK)

    def put(self, request, format=None):
        queryset = Unit.objects.get(id=request.data['id'])
        if request.data['check_in_permission_nid'] == '' or request.data['check_in_permission_nid'] is None:
            request.data['check_in_permission_nid'] = 0
        serializer = UnitSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response({'success': True}, status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        user = self.get_object(request.user.pk)
        owner = Owner.objects.get(user=user)
        queryset = Unit.objects.get(id=request.GET.get('id'))
        if user and owner and queryset:
            owner.unit.remove(queryset)
            owner.save()
            queryset.delete()
            return Response({'success': True}, status=status.HTTP_200_OK)
        return Response({'success': False, 'message': "Member not found"}, status=status.HTTP_204_NO_CONTENT)


class ToLetStatus(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, ]

    def put(self, request, id, format=None):
        unit = Unit.objects.get(id=id)
        if unit.status:
            unit.status = False
        else:
            unit.status = True
        unit.save()

        return Response({'success': True}, status=status.HTTP_200_OK)

