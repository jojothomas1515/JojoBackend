from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), unique=True, max_length=100, null=True, blank=True)

    profile_image = models.ImageField(_('Profile Image'), null='True', blank=True,
                                      default='https://firebasestorage.googleapis.com/v0/b/jojopage-001.appspot.com/o/default%2Fno-profile-picture-icon-11.jpg?alt=media&token=7f8f1d08-6ce9-4ef5-b00e-0939e70895ed',
                                      upload_to=f'images/profile', max_length=200)
    email = models.EmailField(_('email address'), unique=True)
    firstname = models.CharField(_('First Name'), max_length=100, null=True, blank=True)
    lastname = models.CharField(_('Last Name'), max_length=100, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
