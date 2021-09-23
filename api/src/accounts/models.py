import datetime

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

from rest_framework.authtoken.models import Token # noqa
from rest_framework_simplejwt.tokens import RefreshToken

from django.db import models
from django.utils.translation import ugettext_lazy as _

from drf_core import fields
from drf_core.models import create_api_key

from accounts.constants import AUTH_PROVIDERS


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        @param email: The email
        @param password: The password
        @param extra_fields:
        @return:
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        @param email: The email
        @param password: The password
        @param extra_fields:
        @return:
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
    User model
    """
    @property
    def is_user(self):
        return hasattr(self, 'role') and self.role in [self.USER_ROLE]

    @property
    def is_admin(self):
        return hasattr(self, 'role') and self.role in [self.ADMIN_ROLE]

    username = None

    email = fields.EmailField(
        null=False,
        unique=True,
        error_messages={'unique': 'This email address is already being used.'},
        help_text='The email of user'
    )

    first_name = fields.NameField(
        null=True,
        help_text='The first name'
    )

    last_name = fields.NameField(
        null=True,
        help_text='The last name'
    )

    auth_provider = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        default=AUTH_PROVIDERS.get('email')
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }


# Automatically generates tastypie API key for the user.
models.signals.post_save.connect(create_api_key, sender=User)
