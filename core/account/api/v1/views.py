from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CustomRegistrationSerializer

class CustomRegistrationApiView(GenericAPIView) :
    serializer_class = CustomRegistrationSerializer

    def post(self,request,*args,**kwargs) :
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            date = {
                "email" : serializer.validated_data["email"]
            }
            return Response(date,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)