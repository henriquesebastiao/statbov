from django.db import models


class EmploymentUser(models.Model):
    user_id = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    employment_id = models.ForeignKey('Employment', on_delete=models.PROTECT)

    class Meta:
        indexes = [
            models.Index(
                fields=['user_id'], name='user_id_employment_user_idx'
            ),
            models.Index(fields=['employment_id'], name='employment_id_idx'),
        ]

    def __str__(self):
        return f'{self.user_id} - {self.employment_id}'
