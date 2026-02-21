from django.contrib.auth.models import (AbstractBaseUser,PermissionsMixin,BaseUserManager)
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

class UserManager(BaseUserManager) :
    def create_user(self,email,password,**extra_fields) :
        if not email :
            raise ValueError(_("The email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password,**extra_fields) :
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_active",True)
        extra_fields.setdefault("is_verified",True)

        if extra_fields.get("is_superuser") is not True :
            raise ValueError(_("superuser must have is_superuser = True"))
        if extra_fields.get("is_staff") is not True :
            raise ValueError(_("superuser must have is_staff = True"))
        if extra_fields.get("is_active") is not True :
            raise ValueError(_("superuser must have is_active = True"))
        if extra_fields.get("is_verified") is not True :
            raise ValueError("superuser must have is_superuser = True")
        
        return self.create_user(email,password,**extra_fields)

class User(AbstractBaseUser,PermissionsMixin) :
    email = models.EmailField(max_length=255,unique=True,verbose_name=_("email"))
    is_superuser = models.BooleanField(default=False,verbose_name=_("super user"))
    is_staff = models.BooleanField(default=False,verbose_name=_("staff"))
    is_active = models.BooleanField(default=True,verbose_name=_("active"))
    is_verified = models.BooleanField(default=False,verbose_name=_("verified"))

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self) :
        return self.email
    
class Profile(models.Model) :
    user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name=_("user"))
    first_name = models.CharField(max_length=55,verbose_name=_("first name"))
    last_name = models.CharField(max_length=55,verbose_name=_("last name"))
    image = models.ImageField(blank=True,null=True)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.user.email
    
@receiver(post_save,sender=User)
def save_profile(sender,instance,created,**kwargs) :
    if created :
        Profile.objects.create(user=instance)