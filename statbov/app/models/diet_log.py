from django.db import models


class DietLog(models.Model):
    diet_id = models.ForeignKey('Diet', on_delete=models.CASCADE)
    batch_id = models.ForeignKey('Batch', on_delete=models.CASCADE)
    init_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['diet_id'], name='diet_id_diet_log_idx'),
            models.Index(fields=['batch_id'], name='batch_id_diet_log_idx'),
            models.Index(fields=['init_date'], name='init_date_idx'),
            models.Index(fields=['end_date'], name='end_date_idx'),
        ]
        unique_together = ['diet_id', 'batch_id']
