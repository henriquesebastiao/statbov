from datetime import date

from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from statbov.app.models import Animal, Batch, BatchLog

from ..utils import ModelAttrsTest, ModelTest


class BatchLogModelTestBase(ModelTest):
    fixtures = ['batch_log']

    @classmethod
    def setUpTestData(cls):
        cls.MODEL = BatchLog
        cls.ATTRS = ModelAttrsTest(
            id=1,
            animal_id=Animal.objects.get(pk=1),
            batch_id=Batch.objects.get(pk=1),
            entry_date_batch='2020-01-01',
            exit_date_batch='2020-01-01',
        )


class BatchLogModelTestCreateSuccess(BatchLogModelTestBase):
    def test_creation_batch_log_success(self):
        batch_log = self.create_instance()
        self.assertTrue(isinstance(batch_log, BatchLog))


class BatchLogModelTestAnimalId(BatchLogModelTestBase):
    def test_creation_batch_log_without_animal_id(self):
        with self.assertRaises(IntegrityError):
            self.create_instance(animal_id=None)

    def test_creation_batch_log_blank_animal_id(self):
        with self.assertRaises(ValueError):
            self.create_instance(animal_id='')

    def test_creation_batch_log_invalid_animal_id(self):
        with self.assertRaises(ValueError):
            self.create_instance(animal_id='a')

    def test_creation_batch_log_nonexistent_animal_id(self):
        try:
            self.create_instance(animal_id=Animal.objects.get(pk=999))
        except Animal.DoesNotExist:
            self.assertTrue(True)


class BatchLogModelTestBatchId(BatchLogModelTestBase):
    def test_creation_batch_log_without_batch_id(self):
        with self.assertRaises(IntegrityError):
            self.create_instance(batch_id=None)

    def test_creation_batch_log_blank_batch_id(self):
        with self.assertRaises(ValueError):
            self.create_instance(batch_id='')

    def test_creation_batch_log_invalid_batch_id(self):
        with self.assertRaises(ValueError):
            self.create_instance(batch_id='a')

    def test_creation_batch_log_nonexistent_batch_id(self):
        try:
            self.create_instance(batch_id=Batch.objects.get(pk=999))
        except Batch.DoesNotExist:
            self.assertTrue(True)


class BatchLogModelTestEntryDateBatch(BatchLogModelTestBase):
    def test_creation_batch_log_without_entry_date_auto_now_add(self):
        batch_log = self.create_instance(entry_date_batch=None)
        self.assertTrue(isinstance(batch_log, BatchLog))
        self.assertEqual(
            BatchLog.objects.get(pk=1).entry_date_batch, date.today()
        )

    def test_creation_batch_log_blank_entry_date_batch(self):
        batch_log = self.create_instance(entry_date_batch='')
        self.assertTrue(isinstance(batch_log, BatchLog))
        self.assertEqual(
            BatchLog.objects.get(pk=1).entry_date_batch, date.today()
        )

    def test_creation_batch_log_invalid_entry_date_batch(self):
        batch_log = self.create_instance(entry_date_batch='a')
        self.assertTrue(isinstance(batch_log, BatchLog))
        self.assertEqual(
            BatchLog.objects.get(pk=1).entry_date_batch, date.today()
        )


class BatchLogModelTestExitDateBatch(BatchLogModelTestBase):
    def test_creation_batch_log_without_exit_date_batch(self):
        batch_log = self.create_instance(exit_date_batch=None)
        self.assertTrue(isinstance(batch_log, BatchLog))
        self.assertEqual(BatchLog.objects.get(pk=1).exit_date_batch, None)

    def test_creation_batch_log_blank_exit_date_batch(self):
        with self.assertRaises(ValidationError):
            self.create_instance(exit_date_batch='')

    def test_creation_batch_log_invalid_exit_date_batch(self):
        with self.assertRaises(ValidationError):
            self.create_instance(exit_date_batch='a')
