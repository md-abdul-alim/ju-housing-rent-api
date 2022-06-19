from django.shortcuts import render

# Create your views here.
class ProfileAPI(APIView):
    permission_classes = []
    """
    Post, get, put or delete a team instance.
    """
    def get_object(self, uid):
        try:
            return Team.objects.get(uid=uid)
        except Team.DoesNotExist:
            raise Http404

    def post(self, request):
        serializer = TeamRegistrationSerializer(data=request.data)
        if Team.objects.filter(name=request.data['name']).exists():
            msg = {'success': False, 'message': 'This team is already exist.'}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.is_valid():
                team=serializer.save()
                team.company=request.user.company
                team.save()
                return Response({'success': True}, status=status.HTTP_200_OK)
        return Response({'success': False, "msg": str(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, uid, format=None):
        team = self.get_object(uid)
        serializer = TeamSerializer(team)
        return Response({'success': True, "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, uid, format=None):
        team = self.get_object(uid)
        serializer = TeamRegistrationSerializer(team, data=request.data)
        if serializer.is_valid():
            if Team.objects.filter(name=request.data['name']).exists():
                msg = {'success': False, 'message': 'This team is already exist.'}
                return Response(msg, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response({'success': True}, status=status.HTTP_200_OK)
        return Response({'success': False, "message": 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uid, format=None):
        team = self.get_object(uid)
        team.delete()
        return Response({'success': True}, status=status.HTTP_204_NO_CONTENT)