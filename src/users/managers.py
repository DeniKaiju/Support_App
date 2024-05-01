from typing import Any
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password



class UserManager(BaseUserManager):
    def create_user(
            self, 
            email: str, 
            password: str | None = None, 
            **extra_fields,
    ):
        user = self.model(email=self.normalize_email(email), **extra_fields)
        setattr(user, "password", make_password(password))

        user.save()

        pass

    def create_superuser(
            self, 
            email: str, 
            password: str | None = None, 
            **extra_fields,
    ):
        pass