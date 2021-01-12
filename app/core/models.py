from django.db import models
from django.contrib.auth.models import BaseUserManager,PermissionsMixin,AbstractBaseUser

# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self,email,password=None,**kwargs):
        if not email:
            raise ValueError('user must have email address')
        usr=self.model(email=email,**kwargs)
        usr.set_password(password)
        usr.save(using=self._db)
        return usr

    def create_superuser(self,email,password):
        user=self.model(email=email)
        user.set_password(password)
        user.is_staff=True
        user.is_superuser=True
        user.save()
        return user

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD ='email'