from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from statbov.app.models import Batch, Diet, DietLog

from ..utils import ModelAttrsTest, ModelTest


class DietLogModelTestBase(ModelTest):
    fixtures = ['batch', 'diet_log']

    @classmethod
    def setUpTestData(cls):
        cls.MODEL = DietLog
        cls.ATTRS = ModelAttrsTest(
            diet_id=Diet.objects.get(pk=1),
            batch_id=Batch.objects.get(pk=1),
            init_date='2020-01-01',
            end_date='2020-01-01',
        )


class DietLogModelTestCreateSuccess(DietLogModelTestBase):
    def test_creation_diet_log_success(self):
        diet_log = self.create_instance()
        self.assertTrue(isinstance(diet_log, DietLog))


class DietLogModelTestDietId(DietLogModelTestBase):
    def test_creation_diet_log_without_diet_id(self):
        with self.assertRaises(IntegrityError):
            self.create_instance(diet_id=None)

    def test_creation_diet_log_blank_diet_id(self):
        with self.assertRaises(ValueError):
            self.create_instance(diet_id='')

    def test_creation_diet_log_invalid_diet_id(self):
        with self.assertRaises(ValueError):
            self.create_instance(diet_id='a')

    def test_creation_diet_log_nonexistent_diet_id(self):
        try:
            self.create_instance(diet_id=Diet.objects.get(pk=999))
        except Diet.DoesNotExist:
            self.assertTrue(True)


class DietLogModelTestBatchId(DietLogModelTestBase):
    def test_creation_diet_log_without_batch_id(self):
        with self.assertRaises(IntegrityError):
            self.create_instance(batch_id=None)

    def test_creation_diet_log_blank_batch_id(self):
        with self.assertRaises(ValueError):
            self.create_instance(batch_id='')

    def test_creation_diet_log_invalid_batch_id(self):
        with self.assertRaises(ValueError):
            self.create_instance(batch_id='a')

    def test_creation_diet_log_nonexistent_batch_id(self):
        try:
            self.create_instance(batch_id=Batch.objects.get(pk=999))
        except Batch.DoesNotExist:
            self.assertTrue(True)


class DietLogModelTestEndDate(DietLogModelTestBase):
    def test_creation_diet_log_blank_end_date(self):
        with self.assertRaises(ValidationError):
            self.create_instance(end_date='')

    def test_creation_diet_log_invalid_end_date(self):
        with self.assertRaises(ValidationError):
            self.create_instance(end_date='a')
