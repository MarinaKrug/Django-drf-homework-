from rest_framework.response import Response
from rest_framework.views import APIView
from user_selection.models import User


# Create your views here.
from user_selection.serializers import UserSelectionSerializer


class UserSelectionAPIVIEW(APIView):
    def get(self, request, id):
        lst = User.objects.filter(pk=id)
        return Response({'user': list(lst)})


