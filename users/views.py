from rest_framework.generics import RetrieveAPIView, UpdateAPIView

from api.serializers import UpdateInviteSerializer, UserProfileSerializer
from users.models import User


class UserProfileView(RetrieveAPIView):
    """Информация о профиле пользователя."""

    queryset = User.objects.all()
    serializer_class = UserProfileSerializer


class ActivateInviteView(UpdateAPIView):
    """Активация приглашения."""

    queryset = User.objects.all()
    serializer_class = UpdateInviteSerializer
