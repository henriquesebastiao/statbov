from datetime import date

from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=254, null=True, blank=True)
    creator = models.ForeignKey(
        'CustomUser',
        null=True,
        on_delete=models.SET_NULL,
        related_name='creator',
    )
    responsible = models.ForeignKey(
        'CustomUser', on_delete=models.PROTECT, related_name='responsible'
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=['done'], name='done_idx'),
            models.Index(fields=['responsible'], name='responsible_idx'),
            models.Index(fields=['creator'], name='creator_idx'),
        ]

    def __str__(self):
        return f'{self.title} - {self.responsible.first_name}'

    @property
    def creation_time(self):
        today = date.today()
        return (
            today.year
            - self.creation_date.year
            - (
                (today.month, today.day)
                < (self.creation_date.month, self.creation_date.day)
            )
        )
