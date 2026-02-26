from django.urls import path , include

from . import views

app_name = "api_v1"

urlpatterns = [
    path("api/v1/",include("account.api.v1.urls")),
    path("send-email/",views.send_email,name="send_email")

]