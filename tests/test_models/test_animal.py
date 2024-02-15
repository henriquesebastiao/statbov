from django.core.exceptions import ValidationError
from django.db.utils import DataError

from statbov.app.models import Animal, Farm

from ..utils import ModelAttrsTest, ModelTest


class AnimalModelTestBase(ModelTest):
    fixtures = ['animal']

    @classmethod
    def setUpTestData(cls):
        cls.MODEL = Animal
        cls.ATTRS = ModelAttrsTest(
            id=3,
            farm_origin_id=Farm.objects.get(pk=1),
            race='NL',
            mother_id=Animal.objects.get(pk=1),
            father_id=Animal.objects.get(pk=2),
            gender='M',
            entry_date='2021-01-01',
            exit_date='2021-02-01',
            reason_living='SL',
        )


class AnimalModelTestCreateSuccess(AnimalModelTestBase):
    def test_creation_animal_success(self):
        animal = self.create_instance()
        self.assertTrue(isinstance(animal, Animal))


class AnimalModelTestFarmOriginId(AnimalModelTestBase):
    def test_creation_animal_without_farm_origin_id(self):
        with self.assertRaises(ValidationError):
            self.create_instance(farm_origin_id=None)

    def test_creation_animal_blank_farm_origin_id(self):
        with self.assertRaises(ValueError):
            self.create_instance(farm_origin_id='')

    def test_creation_animal_invalid_farm_origin_id(self):
        with self.assertRaises(ValueError):
            self.create_instance(farm_origin_id='a')

    def test_creation_animal_nonexistent_farm_origin_id(self):
        try:
            self.create_instance(farm_origin_id=Farm.objects.get(pk=999))
        except Farm.DoesNotExist:
            self.assertTrue(True)


class AnimalModelTestRace(AnimalModelTestBase):
    def test_creation_animal_without_race(self):
        with self.assertRaises(ValidationError):
            self.create_instance(race=None)

    def test_creation_animal_blank_race(self):
        with self.assertRaises(ValidationError):
            self.create_instance(race='')

    def test_creation_animal_invalid_race(self):
        with self.assertRaises(ValidationError):
            self.create_instance(race='XX')

    def test_creation_animal_very_long_option_race(self):
        with self.assertRaises(DataError):
            self.create_instance(race='GIR')

    def test_creation_animal_number_race(self):
        with self.assertRaises(ValidationError):
            self.create_instance(race=1)
