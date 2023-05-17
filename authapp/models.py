from django.db import models
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

# Create your models here.
class FndUserManager(BaseUserManager):
    def create_user(self, username, email, first_name, password=None):
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        fndUser = self.model(username=username, email=self.normalize_email(email), first_name=first_name)
        fndUser.set_password(password)
        fndUser.save()

        return fndUser

    def create_superuser(self, username, email, password):
      if password is None:
          raise TypeError('Superusers must have a password.')

      user = self.create_user(username, email, password)
      user.is_superuser = True
      user.is_staff = True
      user.is_verified=True
      user.save()

      return user
 
class FndUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # new field for balance

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = FndUserManager()

    def __str__(self):
        return self.email

    #since we do not store their real name we return their username
    def get_full_name(self):
        return self.username

    #this allows us to return the jwt token by calling user.token method
    def token(self):
        return self.generate_jwt_token()


      #generate token using user emailand username .token is generated during signup  
    def generate_jwt_token(self):
        user_details = {'email':self.email,'username':self.username}
        token = jwt.encode(
            {
                'user_data':user_details,
                'exp':datetime.now() + timedelta(hours=24)
            },settings.SECRET_KEY,algorithm ='HS256'
        )
        
        return token

