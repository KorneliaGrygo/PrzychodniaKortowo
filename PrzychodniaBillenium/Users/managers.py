from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class CustomUserManager(BaseUserManager):

    def create_user(self, email, first_name, second_name, phone_number, password=None):
        """
        Creates and saves a User with the given email, password, firstname and secondname.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            second_name=second_name,
            phone_number=phone_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, second_name, phone_number, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email=email,
            first_name=first_name,
            second_name=second_name,
            phone_number=phone_number,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
