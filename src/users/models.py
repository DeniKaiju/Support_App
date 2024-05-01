from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.utils import timezone
from django.db import models

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=30, unique=True, default="example@example.com")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30) # noqa
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    role = models.CharField(max_length=20, default="user")

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    # Добавляем related_name для поля groups и исправляем обратные запросы
    groups = models.ManyToManyField(Group, related_name="users", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="users", blank=True)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        return f"{self.first_name} {self.last_name}".strip()
    
    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name
    
    def __str__(self):
        if self.first_name and self.last_name:
            return self.get_full_name()
        else:
            return self.email
