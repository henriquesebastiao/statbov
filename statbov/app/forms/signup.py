import re
from dataclasses import dataclass

from django import forms
from django.core.exceptions import ValidationError

from ..models import CustomUser


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
    first_name = forms.CharField(
        required=True,
        label='Nome',
        error_messages={
            'required': 'O nome não pode ficar em branco.',
        },
        widget=forms.TextInput(
            attrs={
                'class': 'form-control rounded-bottom-0 border-bottom-0',
                'id': 'floatingInput',
                'placeholder': 'Nome',
            }
        ),
    )
    last_name = forms.CharField(
        required=True,
        label='Sobrenome',
        error_messages={
            'required': 'O sobrenome não pode ficar em branco.',
        },
        widget=forms.TextInput(
            attrs={
                'class': 'form-control rounded-bottom-0 border-bottom-0',
                'id': 'floatingInput',
                'placeholder': 'Sobrenome',
            }
        ),
    )
    email = forms.EmailField(
        required=True,
        label='Email',
        error_messages={
            'invalid': 'O e-mail é inválido.',
            'required': 'O e-mail não pode ficar em branco.',
        },
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control rounded-0',
                'id': 'floatingInput',
                'placeholder': 'Email',
            }
        ),
    )
    password = forms.CharField(
        required=True,
        label='Senha',
        validators=[strong_password],
        error_messages={
            'invalid': 'A senha deve ter pelo menos um caractere maiúsculo, '
            'um minúsculo, um número e um caractere especial. '
            'O tamanho deve ser de pelo menos 8 caracteres.',
            'required': 'A senha não pode ficar em branco.',
        },
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
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
        ]

        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'E-mail',
            'password': 'Senha',
        }

    def clean_email(self):
        """Validates that the email is unique"""
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError(
                'Já existe um usuário com este e-mail.', code='invalid'
            )
        return email
