from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import UpdateAPIView , RetrieveUpdateAPIView

import jwt
from jwt.exceptions import ExpiredSignatureError , DecodeError

from django.conf import settings
from django.shortcuts import get_object_or_404
# from django.core.mail import send_mail
from mail_templated import send_mail
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import CustomRegistrationSerializer,CustomAuthTokenSerializer,CustomChangePasswordSerializer,ProfileSerializer
from account.models import User , Profile

class CustomRegistrationApiView(GenericAPIView) :
    serializer_class = CustomRegistrationSerializer

    def post(self,request,*args,**kwargs) :
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            email = serializer.validated_data["email"]
            date = {
                "email" : email
            }
            user_obj = get_object_or_404(User,email = email)
            token = self.get_tokens_for_user(user_obj)
            send_mail('email/activation_email.tpl', {'token': token}, 'admin@gmail.com', [email])
            return Response(date,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get_tokens_for_user(self,user) :
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
    
class CustomAuthTokenApiView(GenericAPIView) :
    serializer_class = CustomAuthTokenSerializer

    def post(self,request,*args,**kwargs) :
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token,create = Token.objects.get_or_create(user=user)
        return Response({
            "token":token.key,
            "user_id":user.pk,
            "email":user.email
        },status=status.HTTP_200_OK)


class CustomDiscardAuthTokenApiView(APIView) :
    permission_classes = [IsAuthenticated]

    def post(self,request) :
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CustomChangePasswordApiView(UpdateAPIView) :
    permission_classes = [IsAuthenticated]
    model = User
    serializer_class = CustomChangePasswordSerializer

    def get_object(self,queryset=None) :
        obj = self.request.user
        return obj
    
    def update(self,request,*args,**kwargs) :
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid() :
            if not self.object.check_password(serializer.data.get("old_password")) :
                raise Response({"old password":["wrong password"]},status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({"detail":"password chenged successfully"},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class ProfileApiView(RetrieveUpdateAPIView) :
    serializer_class = ProfileSerializer
    queryset = Profile.objects.select_related("user").all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset,user=self.request.user)
        return obj
    
class TestEmailSend(GenericAPIView) :

    def post(self,request,*args,**kwargs) :
        # send_mail(
        #     "Subject here",
        #     "Here is the message.",
        #     "from@example.com",
        #     ["to@example.com"],
        #     fail_silently=False,)
        self.email = 'programmer.py.mail@gmail.com'
        user_obj = get_object_or_404(User,email = self.email)
        token = self.get_tokens_for_user(user_obj)
        send_mail('email/hello.tpl', {'token': token}, 'admin@gmail.com', [self.email])
        return Response("email sent")
    
    def get_tokens_for_user(self,user) :
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

class ActivationApiView(APIView) :

    def get(self,request,token,*args,**kwargs) :
        try :    
            token_obj = jwt.decode(token,settings.SECRET_KEY,algorithms=["HS256"])
            user_id = token_obj.get("user_id")
        except ExpiredSignatureError :
            return Response({"detail":"token has been expired"},status=status.HTTP_400_BAD_REQUEST)
        except DecodeError :
            return Response({"detail":"token is not valid"},status=status.HTTP_400_BAD_REQUEST)
        user_obj = User.objects.get(pk = user_id)
        if user_obj.is_verified :
            return Response({"detail":"your account has already been verified"})
        user_obj.is_verified = True
        user_obj.save()
        return Response({"detail":"your account have been verified and activated successfully"})
