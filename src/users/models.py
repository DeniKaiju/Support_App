from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    avatar = models.CharField(max_length=255)
    level = models.IntegerField(default=1)
