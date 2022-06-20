from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from account.models import User
from renter.models import Renter
from renter.serializers import RenterSerializer
from account.serializers import RegistrationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


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

    def put(self, request, pk, format=None):
        team = self.get_object(pk)
        serializer = RegistrationSerializer(team, data=request.data)
        if serializer.is_valid():
            if User.objects.filter(name=request.data['name']).exists():
                msg = {'success': False, 'message': 'This team is already exist.'}
                return Response(msg, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response({'success': True}, status=status.HTTP_200_OK)
        return Response({'success': False, "message": 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        team = self.get_object(pk)
        team.delete()
        return Response({'success': True}, status=status.HTTP_204_NO_CONTENT)

