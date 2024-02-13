from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(
        self,
        first_name,
        last_name,
        email,
        password,
        **extra_fields,
    ):
        if not first_name:
            raise ValueError(_('The First Name must be set'))
        if not last_name:
            raise ValueError(_('The Last Name must be set'))
        if not email:
            raise ValueError(_('The Email must be set'))
        if not password:
            raise ValueError(_('The Password must be set'))

        email = self.normalize_email(email)
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra_fields,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self,
        first_name,
        last_name,
        email,
        password,
        **extra_fields,
    ):
        if not first_name:
            raise ValueError(_('The First Name must be set'))
        if not last_name:
            raise ValueError(_('The Last Name must be set'))
        if not email:
            raise ValueError(_('The Email must be set'))
        if not password:
            raise ValueError(_('The Password must be set'))

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
