from django.test import TestCase

from statbov.app.forms import SignupForm


class SignupTestFormBase(TestCase):
    data = {
        'first_name': 'Test',
        'last_name': 'User',
        'email': 'testuser@example.com',
        'password': 'Test@1234',
    }

    def mixin_validate_form(
        self, string_to_validate: str, *args: str
    ) -> SignupForm:
        data = self.data.copy()

        for field in args:
            data[field] = string_to_validate

        return SignupForm(data=data)


class SignupTestForm(SignupTestFormBase):
    def test_signup_valid_form(self):
        form = SignupForm(data=self.data)
        self.assertTrue(form.is_valid())


class SignupTestFormPassword(SignupTestFormBase):
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


class SignupTestFormFirstName(SignupTestFormBase):
    def test_signup_invalid_form_witch_blank_first_name(self):
        form = self.mixin_validate_form('', 'first_name')
        self.assertFalse(form.is_valid())


class SignupTestFormLastName(SignupTestFormBase):
    def test_signup_invalid_form_witch_blank_last_name(self):
        form = self.mixin_validate_form('', 'last_name')
        self.assertFalse(form.is_valid())


class SignupTestFormEmail(SignupTestFormBase):
    def test_signup_invalid_form_witch_blank_email(self):
        form = self.mixin_validate_form('', 'email')
        self.assertFalse(form.is_valid())

    def test_signup_invalid_form_witch_invalid_email(self):
        form = self.mixin_validate_form('testuser', 'email')
        self.assertFalse(form.is_valid())
