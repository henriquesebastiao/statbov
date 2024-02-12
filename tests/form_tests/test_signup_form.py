from django.test import TestCase

from statbov.app.forms import SignupForm


class SignupTestForm(TestCase):
    data = {
        'username': 'testuser',
        'password': 'Test123@',
    }

    def mixin_validate_form(
        self, string_to_validate: str, *args: str
    ) -> SignupForm:
        data = self.data.copy()

        for field in args:
            data[field] = string_to_validate

        return SignupForm(data=data)

    def test_signup_valid_form(self):
        form = SignupForm(data=self.data)
        self.assertTrue(form.is_valid())

    def test_signup_invalid_form_witch_weak_password(self):
        form = self.mixin_validate_form('test', 'password')
        self.assertFalse(form.is_valid())

    def test_signup_invalid_form_witch_blank_password(self):
        form = self.mixin_validate_form('', 'password')
        self.assertFalse(form.is_valid())

    def test_signup_invalid_form_witch_password_shorter_than_eight_characters(
        self,
    ):
        form = self.mixin_validate_form('A1@a', 'password')
        self.assertFalse(form.is_valid())

    def test_signup_invalid_form_witch_password_without_numbers(self):
        form = self.mixin_validate_form('Test@abc', 'password')
        self.assertFalse(form.is_valid())

    def test_signup_invalid_form_witch_password_without_uppercase_letters(
        self,
    ):
        form = self.mixin_validate_form('test@1234', 'password')
        self.assertFalse(form.is_valid())

    def test_signup_invalid_form_witch_password_without_lowercase_letters(
        self,
    ):
        form = self.mixin_validate_form('TEST@1234', 'password')
        self.assertFalse(form.is_valid())

    def test_signup_invalid_form_witch_password_without_special_characters(
        self,
    ):
        form = self.mixin_validate_form('Test1234', 'password')
        self.assertFalse(form.is_valid())

    def test_signup_invalid_form_witch_blank_username(self):
        form = self.mixin_validate_form('', 'username')
        self.assertFalse(form.is_valid())
