from django.core.exceptions import ValidationError
from django.db.utils import DataError

from statbov.app.models import Diet

from ..utils import ModelAttrsTest, ModelTest


class DietModelTestBase(ModelTest):
    @classmethod
    def setUpTestData(cls):
        cls.MODEL = Diet
        cls.ATTRS = ModelAttrsTest(
            name='Teste',
            description='Teste',
        )


class DietModelTestCreateSuccess(DietModelTestBase):
    def test_creation_diet_success(self):
        diet = self.create_instance()
        self.assertTrue(isinstance(diet, Diet))


class DietModelTestName(DietModelTestBase):
    def test_creation_diet_without_name(self):
        with self.assertRaises(ValidationError):
            self.create_instance(name=None)

    def test_creation_diet_blank_name(self):
        with self.assertRaises(ValidationError):
            self.create_instance(name='')

    def test_creation_diet_very_long_name(self):
        with self.assertRaises(DataError):
            self.create_instance(name='a' * 21)


class DietModelTestDescription(DietModelTestBase):
    def test_creation_diet_without_description(self):
        with self.assertRaises(ValidationError):
            self.create_instance(description=None)

    def test_creation_diet_blank_description(self):
        with self.assertRaises(ValidationError):
            self.create_instance(description='')

    def test_creation_diet_very_long_description(self):
        with self.assertRaises(DataError):
            self.create_instance(description='a' * 255)
