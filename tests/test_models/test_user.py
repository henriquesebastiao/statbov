from django.core.exceptions import ValidationError

from statbov.app.models import CustomUser

from ..utils import ModelAttrsTest, ModelTest


class CustomUserModelTestBase(ModelTest):
    @classmethod
    def setUpTestData(cls):
        cls.MODEL = CustomUser
        cls.ATTRS = ModelAttrsTest(
            first_name='Test',
            last_name='User',
            email='testuser@example.com',
            birth_date='1990-01-01',
            password='testpassword',
            gender='M',
        )


class CustomUserModelTestCreateSuccess(CustomUserModelTestBase):
    def test_creation_user_success(self):
        user = self.create_instance()
        self.assertTrue(isinstance(user, CustomUser))


class CustomUserModelTestFirstName(CustomUserModelTestBase):
    def test_creation_user_without_first_name(self):
        with self.assertRaises(TypeError):
            self.create_instance(first_name=None)

    def test_creation_user_blank_first_name(self):
        with self.assertRaises(ValueError):
            self.create_instance(first_name='')


class CustomUserModelTestLastName(CustomUserModelTestBase):
    def test_creation_user_without_last_name(self):
        with self.assertRaises(TypeError):
            self.create_instance(last_name=None)

    def test_creation_user_blank_last_name(self):
        with self.assertRaises(ValueError):
            self.create_instance(last_name='')


class CustomUserModelTestEmail(CustomUserModelTestBase):
    def test_creation_user_without_email(self):
        with self.assertRaises(TypeError):
            self.create_instance(email=None)

    def test_creation_user_blank_email(self):
        with self.assertRaises(ValueError):
            self.create_instance(email='')


class CustomUserModelTestBirthDate(CustomUserModelTestBase):
    def test_creation_user_without_birth_date(self):
        user = self.create_instance(birth_date=None)
        self.assertTrue(isinstance(user, CustomUser))

    def test_creation_user_blank_birth_date_success(self):
        user = self.create_instance()
        self.assertTrue(isinstance(user, CustomUser))


class CustomUserModelTestPassword(CustomUserModelTestBase):
    def test_creation_user_without_password(self):
        with self.assertRaises(TypeError):
            self.create_instance(password=None)

    def test_creation_user_blank_password(self):
        with self.assertRaises(ValueError):
            self.create_instance(password='')


class CustomUserModelTestGender(CustomUserModelTestBase):
    def test_creation_user_without_gender(self):
        user = self.create_instance(gender=None)
        self.assertTrue(isinstance(user, CustomUser))

    def test_creation_user_blank_gender(self):
        user = self.create_instance(gender='')
        self.assertTrue(isinstance(user, CustomUser))

    def test_creation_user_with_invalid_gender(self):
        with self.assertRaises(ValidationError):
            self.create_instance(gender='X')
