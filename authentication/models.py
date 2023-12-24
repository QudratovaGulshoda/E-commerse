from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    first_name = models.CharField(
        max_length=150, verbose_name="First Name", null=True, blank=True)
    last_name = models.CharField(
        max_length=150, verbose_name="Last Name", null=True, blank=True)
    phone_number = models.CharField(
        max_length=13,
        verbose_name="Phone Number",
        unique=True,
        null=True,
        blank=True,
    )
    avatar = models.ImageField(
        null=True, blank=True, upload_to="avatar_pics/", verbose_name="Avatar Picture"
    )
