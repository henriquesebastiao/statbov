from django import forms


class LoginForm(forms.Form):
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
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control rounded-top-0 border-top-0 border-end-0',
                'id': 'floatingPassword',
                'placeholder': 'Senha',
            }
        ),
    )
