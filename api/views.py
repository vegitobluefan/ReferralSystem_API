import random

from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from referral_system.settings import MAX_RANDINT, MIN_RANDINT, TIMEOUT
from users.models import User


class LoginView(APIView):
    """Рассылка кода на номер телефона."""

    def post(self, request):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response(
                {"error": "Введите номер телефона"},
                status=HTTP_400_BAD_REQUEST
            )
        auth_code = random.randint(MIN_RANDINT, MAX_RANDINT)
        cache.set(f'auth_code_{phone_number}', auth_code, timeout=TIMEOUT)
        return Response({"Код": auth_code})


class VerifyCodeView(APIView):
    """Верификация кода и логин пользователя.."""

    def post(self, request):
        phone_number = request.data.get('phone_number')
        code = request.data.get('code')

        if not phone_number or not code:
            return Response(
                {"error": "Неверный  номер телефона или код"},
                status=HTTP_400_BAD_REQUEST)

        cached_code = cache.get(f'auth_code_{phone_number}')
        if str(cached_code) != str(code):
            return Response(
                {"error": "Неверный код"}, status=HTTP_400_BAD_REQUEST
            )
        user, created = User.objects.get_or_create(phone_number=phone_number)
        return Response({"message": "Успешно", "id пользователя": user.id})
