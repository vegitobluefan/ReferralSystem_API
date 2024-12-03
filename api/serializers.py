from rest_framework import serializers

from users.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    """Сериализатор для профиля пользователя."""

    referrals = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = (
            'id', 'phone_number', 'invite_code', 'referred_by', 'referrals',
        )


class UpdateInviteSerializer(serializers.ModelSerializer):
    """Сериализатор для рефералов."""

    class Meta:
        model = User
        fields = ('referred_by',)

    def validate_referred_by(self, value):
        if not User.objects.filter(id=value.id).exists():
            raise serializers.ValidationError('Неверный код')
        return value
