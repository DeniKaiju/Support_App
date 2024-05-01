# Generated by Django 4.2.11 on 2024-05-01 15:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")), # noqa
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "email",
                    models.CharField(
                        default="example@example.com", max_length=30, unique=True # noqa
                    ),
                ),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "date_joined", # noqa
                    models.DateTimeField(default=django.utils.timezone.now), # noqa
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True, related_name="users", to="auth.group"
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True, related_name="users", to="auth.permission"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
