from django.urls import path

from api.views import LoginView, VerifyCodeView
from users.views import ActivateInviteView, UserProfileView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('verify/', VerifyCodeView.as_view(), name='verify'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path(
        'profile/<int:pk>/activate-invite/',
        ActivateInviteView.as_view(),
        name='activate_invite'
    ),
]
