from django.test import TestCase

from statbov.app.forms import LoginForm


class LoginTestForm(TestCase):
    data = {
        'email': 'test@user.com',
        'password': 'Test@1234',
    }

    def mixin_validate_form(
        self, string_to_validate: str, *args: str
    ) -> LoginForm:
        data = self.data.copy()

        for field in args:
            data[field] = string_to_validate

        return LoginForm(data=data)

    def test_login_valid_form(self):
        form = LoginForm(data=self.data)
        self.assertTrue(form.is_valid())

    def test_login_invalid_form_witch_blank_email(self):
        form = self.mixin_validate_form('', 'email')
        self.assertFalse(form.is_valid())

    def test_login_invalid_form_witch_blank_password(self):
        form = self.mixin_validate_form('', 'password')
        self.assertFalse(form.is_valid())

    def test_login_invalid_form_witch_blank_email_and_password(self):
        form = self.mixin_validate_form('', 'email', 'password')
        self.assertFalse(form.is_valid())
