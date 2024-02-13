from django.test import TestCase, TestCase as DjangoTesteCase
from django.urls import reverse

from statbov.app.forms import SignupForm


class SignupFormUnitTest(TestCase):
    EMAIL_TEXT = 'Email'
    PASSWORD_TEXT = 'Senha'

    def setUp(self):
        self.form = SignupForm()

    # Test placeholders
    def test_email_placeholder_is_correct(self):
        placeholder = self.form.fields['email'].widget.attrs['placeholder']
        self.assertEqual(self.EMAIL_TEXT, placeholder)

    def test_password_placeholder_is_correct(self):
        placeholder = self.form.fields['password'].widget.attrs['placeholder']
        self.assertEqual(self.PASSWORD_TEXT, placeholder)

    # Test labels
    def test_email_label_is_correct(self):
        label = self.form.fields['email'].label
        self.assertEqual(self.EMAIL_TEXT, label)

    def test_password_label_is_correct(self):
        label = self.form.fields['password'].label
        self.assertEqual(self.PASSWORD_TEXT, label)


class SignupFormIntegrationTeste(DjangoTesteCase):
    def setUp(self):
        self.form_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'birth_date': '1990-01-01',
            'password': 'testpassword',
            'gender': 'M',
        }
        return super().setUp()

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

    def test_user_created_can_login(self):
        self.form_data.update(
            {
                'email': 'testuser@example.com',
                'password': '@Pass123',
            }
        )

        self.client.post(
            reverse('user_create'), data=self.form_data, follow=True
        )

        is_authenticated = self.client.login(
            email=self.form_data.get('email'),
            password=self.form_data.get('password'),
        )

        self.assertTrue(is_authenticated)
