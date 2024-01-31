import re
from dataclasses import dataclass

from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


def strong_password(password):
    """
    Validates that the password is strong enough, if not, raises a ValidationError.

    Args:
        password: The password to be validated.
    """
    regex = re.compile(
        r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!])(?=.*[a-zA-Z0-9@#$%^&+=!]).{8,}$'
    )

    if not regex.match(password):
        raise ValidationError(
            (
                'Password must have at least one uppercase letter, '
                'one lowercase letter and one number. The length should be '
                'at least 8 characters.'
            ),
            code='invalid',
        )


class SignupForm(forms.ModelForm):
    username = forms.CharField(
        required=True,
        label='Nome de usuário',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control rounded-bottom-0',
                'id': 'floatingInputGroup1',
                'placeholder': 'Nome de usuário',
            }
        ),
    )
    password = forms.CharField(
        required=True,
        label='Senha',
        validators=[strong_password],
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control rounded-top-0 border-top-0 border-end-0',
                'id': 'floatingPassword',
                'placeholder': 'Senha',
            }
        ),
    )

    @dataclass
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

        labels = {
            'username': 'Nome de usuário',
            'password': 'Senha',
        }
