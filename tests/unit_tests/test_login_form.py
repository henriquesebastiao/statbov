from unittest import TestCase

from statbov.app.forms import LoginForm


class LoginFormUnitTest(TestCase):
    USERNAME_TEXT = 'Email'
    PASSWORD_TEXT = 'Senha'

    def setUp(self):
        self.form = LoginForm()

    # Test placeholders
    def test_email_placeholder_is_correct(self):
        placeholder = self.form.fields['email'].widget.attrs['placeholder']
        self.assertEqual(self.USERNAME_TEXT, placeholder)

    def test_password_placeholder_is_correct(self):
        placeholder = self.form.fields['password'].widget.attrs['placeholder']
        self.assertEqual(self.PASSWORD_TEXT, placeholder)

    # Test labels
    def test_email_label_is_correct(self):
        label = self.form.fields['email'].label
        self.assertEqual(self.USERNAME_TEXT, label)

    def test_password_label_is_correct(self):
        label = self.form.fields['password'].label
        self.assertEqual(self.PASSWORD_TEXT, label)
