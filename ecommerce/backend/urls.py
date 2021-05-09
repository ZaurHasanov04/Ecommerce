from django.urls import path
from backend.views import *
from backend.password_reset import *


urlpatterns=[
    path('api/user/', UserDetail.as_view()),
    path('api/token/', LoginTokenSerializers.as_view()),
    path('api/register', RegisterViews().as_view()),
    path('api/email/reset', PasswordResetEmail.as_view()),
    path('check_email/', check_email),
    path('api/password_reset/', PasswordReset.as_view())
]