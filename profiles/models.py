from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.is_verify = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    username = models.CharField(verbose_name='username', max_length=20, unique=True)
    avatar = models.ImageField(upload_to='media/avatars/', null=True, blank=True)  # , default='media/avatars/default_avatar.png'
    description = models.TextField(max_length=255, null=True, blank=True)
    user_admin_description = models.TextField(max_length=255, null=True, blank=True)
    is_verify = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    objects = MyUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin


class VerifyUser(models.Model):
    username = models.CharField(verbose_name='??????', max_length=255, blank=True)
    phone = models.CharField(verbose_name='??????????????', max_length=255, blank=True)
    email = models.EmailField(verbose_name='??????????', max_length=255, blank=True)
    text = models.TextField(verbose_name='?? ????????', blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{} {}'.format(self.author, self.phone)

    class Meta:
        verbose_name = '????????????'
        verbose_name_plural = '????????????'

