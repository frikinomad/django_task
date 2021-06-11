from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self,email,username,address,password=None):
        if not email:
            raise ValueError('Users must have an email address')

        email=self.normalize_email(email)
        user = self.model(email=email,username=username,address=address)
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self, email, username, address, password):
        user = self.create_user(email,username,address,password)
        user.is_admin = True
        user.save(using=self._db)

        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True,)
    username = models.CharField(max_length=50)
    address = models.TextField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'address']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin