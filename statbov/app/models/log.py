from django.db import models


class Log(models.Model):
    user_id = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=20)
    description = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['user_id'], name='user_id_log_idx'),
            models.Index(fields=['datetime'], name='datetime_log_idx'),
        ]

    def __str__(self):
        return f'{self.datetime} - {self.user_id.username} - {self.action}'
