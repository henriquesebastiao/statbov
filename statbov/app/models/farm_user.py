from django.db import models


class FarmUser(models.Model):
    user_id = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    farm_id = models.ForeignKey('Farm', on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['user_id'], name='user_id_farm_user_idx'),
            models.Index(fields=['farm_id'], name='farm_id_farm_user_idx'),
        ]
        unique_together = ('user_id', 'farm_id')

    def __str__(self):
        return f'{self.user_id.name} - {self.farm_id.name}'
