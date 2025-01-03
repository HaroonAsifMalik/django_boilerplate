import random

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.deconstruct import deconstructible
from django_extensions.db.models import TimeStampedModel

from accounts.managers import CustomUserManager


@deconstructible
class RandomAvatar:
    def __init__(self):
        self.avatar = [
            "avatars/1.png",
            "avatars/2.png",
            "avatars/3.png",
            "avatars/4.png",
            "avatars/5.png",
        ]

    def __call__(self):
        return random.choice(self.avatar)


class CustomUser(AbstractUser, TimeStampedModel):
    username = None
    GOOGLE = "google"

    PROVIDER_CHOICES = [
        ("google", GOOGLE),
    ]
    provider = models.CharField(
        max_length=255, choices=PROVIDER_CHOICES, blank=True, null=True
    )

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(
        upload_to="user_images/", blank=True, null=True, default=RandomAvatar()
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email
