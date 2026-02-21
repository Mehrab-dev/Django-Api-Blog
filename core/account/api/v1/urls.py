from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,TokenVerifyView)

from . import views

app_name = "account"

urlpatterns = [
    path("register/token/",views.CustomRegistrationApiView.as_view(),name="register"),
    path("login/token/",views.CustomAuthTokenApiView.as_view(),name="login_token"),
    path("logout/token/",views.CustomDiscardAuthTokenApiView.as_view(),name="logout_token"),

    # authentication with jwt
    path("create/jwt/",TokenObtainPairView.as_view(),name="create_jwt"),
    path("refresh/jwt/",TokenRefreshView.as_view(),name="refresh_jwt"),
    path("verify/jwt/",TokenVerifyView.as_view(),name="verify_jwt"),

    # change password
    path("change-password/",views.CustomChangePasswordApiView.as_view(),name="change_password"),

    # profile
    path("profile/",views.ProfileApiView.as_view(),name="profile"),

]