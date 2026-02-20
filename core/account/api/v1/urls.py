from django.urls import path

from . import views

app_name = "account"

urlpatterns = [
    path("register/token/",views.CustomRegistrationApiView.as_view(),name="register"),

]