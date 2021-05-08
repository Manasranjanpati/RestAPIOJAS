from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager, PermissionsMixin)
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
class AssetData(models.Model):
    asset_no = models.IntegerField(primary_key=True)
    asset_name = models.CharField(max_length=100)
    asset_price = models.FloatField()
    asset_quantity = models.IntegerField()


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('The given user must me set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email=None,password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None,password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser have to have permission is_staff=True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have to have is_superuser=True')

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200,unique=True, null=True)
    email = models.EmailField(max_length=254, unique=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)


USERNAME_FIELD ="email"
REQUIRED_FIELD =[]