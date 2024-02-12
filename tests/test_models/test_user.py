from django.test import TestCase

from statbov.app.models import CustomUser


class CustomUserModelTest(TestCase):
    def test_creation_user_success(self):
        user = CustomUser.objects.create_user(
            username='testuser',
            first_name='Test',
            last_name='User',
            email='testuser@example.com',
            birth_date='1990-01-01',
            password='testpassword',
            gender='M',
        )

        self.assertTrue(isinstance(user, CustomUser))

    def test_creation_user_without_first_name(self):
        with self.assertRaises(TypeError):
            CustomUser.objects.create_user(
                username='testuser',
                last_name='User',
                email='testuser@example.com',
                birth_date='1990-01-01',
                password='testpassword',
                gender='M',
            )

    def test_creation_user_blank_first_name(self):
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(
                username='testuser',
                first_name='',
                last_name='User',
                email='testuser@example.com',
                birth_date='1990-01-01',
                password='testpassword',
                gender='M',
            )
