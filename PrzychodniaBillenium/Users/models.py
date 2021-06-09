from django.db.models import fields

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.forms import ModelForm

# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
            Custom defined user:
            - login is considered as email field.
    """

    first_name = models.CharField(
        max_length=64,
        help_text=_('Enter the first name: ')
    )

    second_name = models.CharField(
        max_length=64,
        help_text=_('Enter the second name: ')
    )

    phone_number = models.CharField(
        max_length=12,
        help_text=_('Enter the phone number: ')
    )

    email = models.EmailField(
        max_length=64,
        verbose_name=_('email address'),
        help_text=_('Enter the email field: '),
        unique=True
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    # default username defined as email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'second_name', 'phone_number']

    # Representing User object as string containing the email
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


def CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'second_name',
            'phone_number',
            'email',
            'password'
        ]
