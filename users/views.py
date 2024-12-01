from rest_framework.generics import RetrieveAPIView, UpdateAPIView

from api.serializers import UpdateInviteSerializer, UserProfileSerializer
from users.models import User


class UserProfileView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer


class ActivateInviteView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateInviteSerializer
