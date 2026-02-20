from django.urls import path , include

app_name = "api_v1"

urlpatterns = [
    path("api/v1/",include("account.api.v1.urls"))

]