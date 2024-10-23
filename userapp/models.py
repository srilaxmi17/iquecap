from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
import random
from datetime import timedelta


# class UserManager(BaseUserManager):
#     def create_user(self, mobile_number=None, password=None, **extra_fields):
#         if not mobile_number:
#             raise ValueError('The Mobile Number must be set')
#         user = self.model(mobile_number=mobile_number, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     def create_superuser(self, mobile_number=None, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(mobile_number, password, **extra_fields)
    
class User(models.Model):
    mobile_number = models.CharField(max_length=15, unique=True,null=True, blank=True)
    uid = models.CharField(max_length=128, unique=True, null=True, blank=True)  # Add uid field for Firebase uid
    name = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    billing_address = models.TextField(blank=True,null=True)
    address = models.TextField(blank=True, null=True)  # Add the address field
    pan_card = models.CharField(max_length=10, blank=True, null=True)
    profile_image = models.CharField(max_length=500, blank=True, null=True)      
    is_mobile_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)  # Ensure this field is present

    # objects = UserManager()

    # USERNAME_FIELD = 'mobile_number'
    # REQUIRED_FIELDS = []
    # USERNAME_FIELD = 'uid'  # Authenticate with UID
    # REQUIRED_FIELDS = [] 

    # def __str__(self):
    #     return self.uid
    

    # def has_perm(self, perm, obj=None):
    #     return self.is_superuser

    # def has_module_perms(self, app_label):
    #     return self.is_superuser    

    

    # @property
    # def tokens(self):
    #     from rest_framework_simplejwt.tokens import RefreshToken
    #     refresh = RefreshToken.for_user(self)
    #     return {
    #         'refresh': str(refresh),
    #         'access': str(refresh.access_token),
    #     }
    
    