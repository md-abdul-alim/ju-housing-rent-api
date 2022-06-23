from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from account.models import User, FamilyMember, EmergencyContact, OtherMember
from renter.models import Renter
from django.contrib.auth.hashers import make_password
from renter.serializers import RenterSerializer
from account.serializers import RegistrationSerializer, FamilyMemberSerializer, EmergencyContactSerializer,\
    OtherMemberSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import QueryDict


class ProfileAPI(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, ]
    """
    Post, get, put or delete a team instance.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if User.objects.filter(username=request.data['email']).exists():
            msg = {'success': False, 'message': 'This User is already exist.'}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.is_valid():
                serializer.save()
                return Response({'success': True}, status=status.HTTP_200_OK)
        return Response({'success': False, "msg": str(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        user = self.get_object(request.user.pk)
        if request.user.owner_status:
            pass
        elif request.user.renter_status:
            queryset = Renter.objects.get(user=user)
            serializer = RenterSerializer(queryset, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'success': False, "msg": 'sd'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        user = self.get_object(request.user.pk)

        request.data['role'] = 'avoid field value'
        if request.data['password'] == '' and request.data['password2'] == '':
            request.data['password'] = 'avoid field value'
            request.data['password2'] = 'avoid field value'

        serializer = RegistrationSerializer(user, data=request.data)
        if serializer.is_valid():
            if request.user.email == request.data['email'] or not User.objects.filter(email=request.data['email']).exists():
                user.username = request.data['email']
                user.first_name = request.data['first_name']
                user.last_name = request.data['last_name']
                if not (request.data['password'] == '' or request.data['password'] == 'avoid field value'):
                    user.password = make_password(request.data['password'], salt=None, hasher='default')
                user.phone = request.data['phone']
                user.passport = request.data['passport']
                user.nid = request.data['nid']
                user.birthday = request.data['birthday']
                user.occupation = request.data['occupation']
                user.occupation_institution = request.data['occupation_institution']
                user.present_address = request.data['present_address']
                user.permanent_address = request.data['permanent_address']
                user.save()
                return Response({'success': True}, status=status.HTTP_200_OK)
            else:
                msg = {'success': False, 'message': 'This User is already exist.'}
                return Response(msg, status=status.HTTP_400_BAD_REQUEST)

        return Response({'success': False, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        team = self.get_object(pk)
        team.delete()
        return Response({'success': True}, status=status.HTTP_204_NO_CONTENT)


class ProfileFamilyMember(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, ]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request):
        user = self.get_object(request.user.pk)
        queryset = FamilyMember.objects.filter(family_members=user)  # Filtering data by related name
        serializer = FamilyMemberSerializer(queryset, many=True)
        list_ = list()
        for family_member_dict in serializer.data:
            family_dict = dict(family_member_dict)
            query_dict = QueryDict(mutable=True)
            query_dict['id'] = family_dict['id']
            query_dict['name'] = family_dict['name']
            query_dict['age'] = family_dict['age']
            query_dict['phone'] = family_dict['phone']
            query_dict['relation'] = family_dict['relation']
            query_dict['occupation'] = family_dict['occupation']
            list_.append(query_dict)

        return Response(list_, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        user = self.get_object(request.user.pk)
        name = request.data["name"]
        age = request.data["age"]
        phone = request.data["phone"]
        relation = request.data["relation"]
        occupation = request.data["occupation"]
        family_member = FamilyMember.objects.create(
            name=name,
            age=age,
            phone=phone,
            relation=relation,
            occupation=occupation
        )
        user.family_member.add(family_member)
        user.save()

        return Response({'success': True}, status=status.HTTP_200_OK)

    def put(self, request, format=None):
        queryset = FamilyMember.objects.get(id=request.data['id'])
        serializer = FamilyMemberSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response({'success': True}, status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        user = self.get_object(request.user.pk)
        if user and request.GET.get('member'):
            queryset = FamilyMember.objects.get(id=request.GET.get('member'))
            user.family_member.remove(queryset)
            user.save()
            queryset.delete()
            return Response({'success': True}, status=status.HTTP_200_OK)
        return Response({'success': False, 'message': "Member not found"}, status=status.HTTP_204_NO_CONTENT)


class ProfileEmergencyContact(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, ]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request):
        user = self.get_object(request.user.pk)
        queryset = EmergencyContact.objects.filter(emergency_contacts=user)  # Filtering data by related name
        serializer = EmergencyContactSerializer(queryset, many=True)
        list_ = list()
        for emergency_contact_dict in serializer.data:
            emergency_dict = dict(emergency_contact_dict)
            query_dict = QueryDict(mutable=True)
            query_dict['id'] = emergency_dict['id']
            query_dict['name'] = emergency_dict['name']
            query_dict['phone'] = emergency_dict['phone']
            query_dict['relation'] = emergency_dict['relation']
            query_dict['address'] = emergency_dict['address']
            list_.append(query_dict)

        return Response(list_, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        user = self.get_object(request.user.pk)
        name = request.data["name"]
        phone = request.data["phone"]
        relation = request.data["relation"]
        address = request.data["address"]
        emergency_contact = EmergencyContact.objects.create(
            name=name,
            phone=phone,
            relation=relation,
            address=address
        )
        user.emergency_contact.add(emergency_contact)
        user.save()

        return Response({'success': True}, status=status.HTTP_200_OK)

    def put(self, request, format=None):
        queryset = EmergencyContact.objects.get(id=request.data['id'])
        serializer = EmergencyContactSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response({'success': True}, status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        user = self.get_object(request.user.pk)
        if user and request.GET.get('member'):
            queryset = EmergencyContact.objects.get(id=request.GET.get('member'))
            user.emergency_contact.remove(queryset)
            user.save()
            queryset.delete()
            return Response({'success': True}, status=status.HTTP_200_OK)
        return Response({'success': False, 'message': "Emergency contact not found"}, status=status.HTTP_204_NO_CONTENT)


class ProfileOtherMember(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, ]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request):
        user = self.get_object(request.user.pk)
        queryset = ''
        if request.GET.get('type') == "cleaner":
            queryset = OtherMember.objects.filter(cleaners=user)  # Filtering data by related name
        elif request.GET.get('type') == "driver":
            queryset = OtherMember.objects.filter(drivers=user)
        serializer = OtherMemberSerializer(queryset, many=True)
        list_ = list()
        for other_member_dict in serializer.data:
            other_dict = dict(other_member_dict)
            query_dict = QueryDict(mutable=True)
            query_dict['id'] = other_dict['id']
            query_dict['name'] = other_dict['name']
            query_dict['age'] = other_dict['age']
            query_dict['phone'] = other_dict['phone']
            query_dict['nid'] = other_dict['nid']
            query_dict['present_address'] = other_dict['present_address']
            query_dict['permanent_address'] = other_dict['permanent_address']
            list_.append(query_dict)

        return Response(list_, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        user = self.get_object(request.user.pk)
        name = request.data["name"]
        age = request.data["age"]
        phone = request.data["phone"]
        nid = request.data["nid"]
        present_address = request.data["present_address"]
        permanent_address = request.data["permanent_address"]
        other_member = OtherMember.objects.create(
            name=name,
            age=age,
            phone=phone,
            nid=nid,
            present_address=present_address,
            permanent_address=permanent_address
        )
        if request.data["type"] == "driver":
            user.driver.add(other_member)
        elif request.data["type"] == "cleaner":
            user.cleaner.add(other_member)
        user.save()

        return Response({'success': True}, status=status.HTTP_200_OK)

    def put(self, request, format=None):
        queryset = OtherMember.objects.get(id=request.data['id'])
        serializer = OtherMemberSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response({'success': True}, status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        user = self.get_object(request.user.pk)
        if user and request.GET.get('member'):
            queryset = OtherMember.objects.get(id=request.GET.get('member'))
            if request.GET.get('type') == 'driver':
                user.driver.remove(queryset)
            elif request.GET.get('type') == 'cleaner':
                user.cleaner.remove(queryset)
            user.save()
            queryset.delete()
            return Response({'success': True}, status=status.HTTP_200_OK)
        return Response({'success': False, 'message': "Emergency contact not found"}, status=status.HTTP_204_NO_CONTENT)
