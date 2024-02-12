from django.db import models


class Batch(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    farm_id = models.ForeignKey('Farm', on_delete=models.CASCADE)
    diet_id = models.ForeignKey('Diet', on_delete=models.PROTECT)
    obs = models.TextField()

    class Meta:
        indexes = [
            models.Index(fields=['farm_id'], name='farm_id_batch_idx'),
            models.Index(fields=['diet_id'], name='diet_id_batch_idx'),
        ]

    def __str__(self):
        return f'Lote: {self.id}'
