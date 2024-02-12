from datetime import date

from django.contrib.auth.models import AbstractUser
from django.db import models

from ..manager import CustomUserManager


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(unique=True, blank=False)
    gender = models.CharField(
        max_length=1, help_text='M - Masculino | F - Feminino', blank=False
    )
    birth_date = models.DateField()

    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'email',
        'birth_date',
        'gender',
    ]

    objects = CustomUserManager()

    class Meta:
        indexes = [
            models.Index(fields=['username'], name='username_idx'),
            models.Index(fields=['email'], name='email_idx'),
        ]

    def __str__(self):
        return self.username

    @property
    def age(self):
        today = date.today()
        return (
            today.year
            - self.birth_date.year
            - (
                (today.month, today.day)
                < (self.birth_date.month, self.birth_date.day)
            )
        )
