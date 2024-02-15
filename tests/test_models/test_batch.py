from django.core.exceptions import ValidationError
from django.db.utils import DataError, IntegrityError

from statbov.app.models import Batch, Diet, Farm

from ..utils import ModelAttrsTest, ModelTest


class BatchModelTestBase(ModelTest):
    fixtures = ['batch']

    @classmethod
    def setUpTestData(cls):
        cls.MODEL = Batch
        cls.ATTRS = ModelAttrsTest(
            id=1,
            farm_id=Farm.objects.get(pk=1),
            diet_id=Diet.objects.get(pk=1),
            obs='Teste',
        )


class BatchModelTestCreateSuccess(BatchModelTestBase):
    def test_creation_batch_success(self):
        batch = self.create_instance()
        self.assertTrue(isinstance(batch, Batch))


class BatchModelTestId(BatchModelTestBase):
    def test_creation_batch_without_id(self):
        with self.assertRaises(ValidationError):
            self.create_instance(id=None)

    def test_creation_batch_blank_id(self):
        with self.assertRaises(ValidationError):
            self.create_instance(id='')

    def test_creation_batch_very_long_id(self):
        with self.assertRaises(DataError):
            self.create_instance(id='a' * 11)


class BatchModelTestFarmId(BatchModelTestBase):
    def test_creation_batch_without_farm_id(self):
        with self.assertRaises(IntegrityError):
            self.create_instance(farm_id=None)

    def test_creation_batch_blank_farm_id(self):
        with self.assertRaises(ValueError):
            self.create_instance(farm_id='')

    def test_creation_batch_invalid_farm_id(self):
        with self.assertRaises(ValueError):
            self.create_instance(farm_id='a')

    def test_creation_batch_nonexistent_farm_id(self):
        try:
            self.create_instance(farm_id=Farm.objects.get(pk=999))
        except Farm.DoesNotExist:
            self.assertTrue(True)


class BatchModelTestDietId(BatchModelTestBase):
    def test_creation_batch_without_diet_id(self):
        with self.assertRaises(IntegrityError):
            self.create_instance(diet_id=None)

    def test_creation_batch_blank_diet_id(self):
        with self.assertRaises(ValueError):
            self.create_instance(diet_id='')

    def test_creation_batch_invalid_diet_id(self):
        with self.assertRaises(ValueError):
            self.create_instance(diet_id='a')

    def test_creation_batch_nonexistent_diet_id(self):
        try:
            self.create_instance(diet_id=Diet.objects.get(pk=999))
        except Diet.DoesNotExist:
            self.assertTrue(True)


class BatchModelTestObs(BatchModelTestBase):
    def test_creation_batch_without_obs(self):
        with self.assertRaises(ValidationError):
            self.create_instance(obs=None)

    def test_creation_batch_blank_obs(self):
        with self.assertRaises(ValidationError):
            self.create_instance(obs='')
