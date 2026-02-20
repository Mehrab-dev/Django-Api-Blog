from rest_framework import serializers

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions

from account.models import User 

class CustomRegistrationSerializer(serializers.ModelSerializer) :
    password1 = serializers.CharField(max_length=55,write_only=True)

    class Meta :
        model = User
        fields = ["email","password","password1"]

    def validate(self, attrs) :
        if attrs.get("password") != attrs.get("password1") :
            raise ValueError(_({"detail":"password does not match"}))    
           
        try :
            validate_password(attrs.get("password"))
        except exceptions.ValidationError as e :
            raise serializers.ValidationError({"password":list(e.messages)})
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop("password1")
        return User.objects.create_user(**validated_data)
        