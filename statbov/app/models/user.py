from datetime import date

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

from ..manager import CustomUserManager


class CustomUser(AbstractUser):
    class GenderOptions(models.TextChoices):
        MA = 'M', 'Masculino'
        FE = 'F', 'Feminino'

    username = None
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(unique=True, blank=False)
    gender = models.CharField(
        max_length=1,
        help_text='M - Masculino | F - Feminino',
        null=True,
        blank=True,
    )
    birth_date = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    class Meta:
        indexes = [
            models.Index(fields=['email'], name='email_idx'),
            models.Index(fields=['first_name'], name='first_name_idx'),
            models.Index(fields=['last_name'], name='last_name_idx'),
        ]

    def __str__(self):
        return self.username

    def clean(self):
        if self.gender and self.gender not in ['M', 'F']:
            raise ValidationError('Gender must be M or F')

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
