from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        # extra_fields are any number of Key Word Arguments(kwargs) something like name for instance
        user = self.model(email=self.normalize_email(email), **extra_fields)  # use to create a new user model using custom user
        user.set_password(password)  # set encrypted password
        user.save(using=self._db)  # self._db supports adding multiple databases to your project(this is best practice)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    # AbstractBaseUser has authentication functionality but NO field
    # PermissionsMixin has functionality for django permissions feature and fields needed for that
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()  # assign a user manager

    USERNAME_FIELD = 'email'
    # replaces the username default field that comes with the default user
    # This is how we want to do our authentication!
