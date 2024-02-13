from django import forms


class LoginForm(forms.Form):
    email = forms.CharField(
        required=True,
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control rounded-bottom-0',
                'id': 'floatingInputGroup1',
                'placeholder': 'Email',
                'autofocus': True,
            }
        ),
    )
    password = forms.CharField(
        required=True,
        label='Senha',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control rounded-top-0 border-top-0 border-end-0',
                'id': 'floatingPassword',
                'placeholder': 'Senha',
            }
        ),
    )
