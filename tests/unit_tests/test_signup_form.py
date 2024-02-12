from django.test import TestCase, TestCase as DjangoTesteCase
from django.urls import reverse

from statbov.app.forms import SignupForm


class SignupFormUnitTest(TestCase):
    USERNAME_TEXT = 'Nome de usuário'
    PASSWORD_TEXT = 'Senha'

    def setUp(self):
        self.form = SignupForm()

    # Test placeholders
    def test_username_placeholder_is_correct(self):
        placeholder = self.form.fields['username'].widget.attrs['placeholder']
        self.assertEqual(self.USERNAME_TEXT, placeholder)

    def test_password_placeholder_is_correct(self):
        placeholder = self.form.fields['password'].widget.attrs['placeholder']
        self.assertEqual(self.PASSWORD_TEXT, placeholder)

    # Test labels
    def test_username_label_is_correct(self):
        label = self.form.fields['username'].label
        self.assertEqual(self.USERNAME_TEXT, label)

    def test_password_label_is_correct(self):
        label = self.form.fields['password'].label
        self.assertEqual(self.PASSWORD_TEXT, label)


class SignupFormIntegrationTeste(DjangoTesteCase):
    def setUp(self):
        self.form_data = {
            'username': 'testuser',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'birth_date': '1990-01-01',
            'password': 'testpassword',
            'gender': 'M',
        }
        return super().setUp()

    def test_field_username_cannot_be_empty(self):
        self.form_data['username'] = ''
        response = self.client.post(
            reverse('user_create'), data=self.form_data, follow=True
        )
        self.assertIn(
            'O nome de usuário não pode ficar em branco.',
            response.content.decode('utf-8'),
        )

    def test_field_password_cannot_be_empty(self):
        self.form_data['password'] = ''
        response = self.client.post(
            reverse('user_create'), data=self.form_data, follow=True
        )
        self.assertIn(
            'A senha não pode ficar em branco.',
            response.content.decode('utf-8'),
        )

    def test_field_password_not_accept_weak_password(self):
        self.form_data['password'] = 'abc'
        response = self.client.post(
            reverse('user_create'), data=self.form_data, follow=True
        )
        self.assertIn(
            'A senha deve ter pelo menos um caractere maiúsculo, '
            'um minúsculo, um número e um caractere especial. '
            'O tamanho deve ser de pelo menos 8 caracteres.',
            response.content.decode('utf-8'),
        )

    def test_field_username_not_register_user_with_email_existing(self):
        form_data_with_username_existing = self.form_data
        self.client.post(
            reverse('user_create'), data=self.form_data, follow=True
        )
        response_with_username_existing = self.client.post(
            reverse('user_create'),
            data=form_data_with_username_existing,
            follow=True,
        )
        self.assertIn(
            'Esse nome de usuário já existe.',
            response_with_username_existing.content.decode('utf-8'),
        )

    def test_user_created_can_login(self):
        self.form_data.update(
            {
                'username': 'tes_tuser',
                'password': '@Pass123',
            }
        )

        self.client.post(
            reverse('user_create'), data=self.form_data, follow=True
        )

        is_authenticated = self.client.login(
            username=self.form_data.get('username'),
            password=self.form_data.get('password'),
        )

        self.assertTrue(is_authenticated)
