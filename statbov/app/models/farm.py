from django.db import models


class Farm(models.Model):
    name = models.CharField(max_length=30)
    farmer_id = models.ForeignKey('Farmer', on_delete=models.PROTECT)

    class Meta:
        indexes = [
            models.Index(fields=['farmer_id'], name='farmer_id_idx'),
        ]

    def __str__(self):
        return self.name
