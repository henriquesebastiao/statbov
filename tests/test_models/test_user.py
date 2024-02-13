from django.core.exceptions import ValidationError
from django.test import TestCase

from statbov.app.models import CustomUser


def _create_user(**kwargs):
    default_args = {
        'username': 'testuser',
        'first_name': 'Test',
        'last_name': 'User',
        'email': 'testuser@example.com',
        'birth_date': '1990-01-01',
        'password': 'testpassword',
        'gender': 'M',
    }

    default_args.update(kwargs)

    # Remove args set to None to test registration attempt without NOT NULL attribute
    for item in kwargs:
        if kwargs[item] is None:
            del default_args[item]

    user = CustomUser.objects.create_user(**default_args)
    user.full_clean()

    return user


class CustomUserModelTest(TestCase):
    def test_creation_user_success(self):
        user = _create_user()
        self.assertTrue(isinstance(user, CustomUser))


class CustomUserModelTestFirstName(TestCase):
    def test_creation_user_without_first_name(self):
        with self.assertRaises(TypeError):
            _create_user(first_name=None)

    def test_creation_user_blank_first_name(self):
        with self.assertRaises(ValueError):
            _create_user(first_name='')


class CustomUserModelTestLastName(TestCase):
    def test_creation_user_without_last_name(self):
        with self.assertRaises(TypeError):
            _create_user(last_name=None)

    def test_creation_user_blank_last_name(self):
        with self.assertRaises(ValueError):
            _create_user(last_name='')


class CustomUserModelTestEmail(TestCase):
    def test_creation_user_without_email(self):
        with self.assertRaises(TypeError):
            _create_user(email=None)

    def test_creation_user_blank_email(self):
        with self.assertRaises(ValueError):
            _create_user(email='')


class CustomUserModelTestBirthDate(TestCase):
    def test_creation_user_without_birth_date(self):
        user = _create_user(birth_date=None)
        self.assertTrue(isinstance(user, CustomUser))

    def test_creation_user_blank_birth_date_success(self):
        user = _create_user()
        self.assertTrue(isinstance(user, CustomUser))


class CustomUserModelTestPassword(TestCase):
    def test_creation_user_without_password(self):
        with self.assertRaises(TypeError):
            _create_user(password=None)

    def test_creation_user_blank_password(self):
        with self.assertRaises(ValueError):
            _create_user(password='')


class CustomUserModelTestGender(TestCase):
    def test_creation_user_without_gender(self):
        user = _create_user(gender=None)
        self.assertTrue(isinstance(user, CustomUser))

    def test_creation_user_blank_gender(self):
        user = _create_user(gender='')
        self.assertTrue(isinstance(user, CustomUser))

    def test_creation_user_with_invalid_gender(self):
        with self.assertRaises(ValidationError):
            _create_user(gender='X')
