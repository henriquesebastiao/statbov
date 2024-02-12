from django.db import models


class BatchLog(models.Model):
    animal_id = models.ForeignKey('Animal', on_delete=models.CASCADE)
    batch_id = models.ForeignKey('Batch', on_delete=models.CASCADE)
    entry_data_batch = models.DateField(auto_now_add=True)
    exit_data_batch = models.DateField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['animal_id'], name='animal_id_batch_log_idx'),
            models.Index(fields=['batch_id'], name='batch_id_batch_log_idx'),
            models.Index(
                fields=['entry_data_batch'], name='entry_data_batch_idx'
            ),
            models.Index(
                fields=['exit_data_batch'], name='exit_data_batch_idx'
            ),
        ]
        unique_together = ['animal_id', 'batch_id']

    def __str__(self):
        return f'{self.animal_id} - {self.batch_id} - {self.entry_data_batch} - {self.exit_data_batch}'
