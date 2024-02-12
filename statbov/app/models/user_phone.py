from django.db import models


class UserPhone(models.Model):
    class PhoneType(models.TextChoices):
        MOBILE = 'MB', 'Celular'
        HOME = 'HM', 'Casa'
        WORK = 'WK', 'Trabalho'

    phone = models.CharField(
        max_length=11, unique=True, help_text='Only numbers'
    )
    user_id = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    phone_type = models.CharField(max_length=2, choices=PhoneType.choices)

    class Meta:
        unique_together = ['phone', 'user_id']
        indexes = [
            models.Index(fields=['user_id'], name='user_id_user_phone_idx'),
        ]

    def __str__(self):
        return self.phone

    @property
    def formatted_phone(self):
        return f'({self.phone[:2]}) {self.phone[2]} {self.phone[3:7]}-{self.phone[7:]}'
