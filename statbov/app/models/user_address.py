from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


class UserAddress(models.Model):
    street = models.CharField(max_length=50)
    number = models.SmallIntegerField(validators=[MinValueValidator(1)])
    cep = models.CharField(
        max_length=8,
        validators=[MinLengthValidator(8)],
        help_text='Only numbers',
    )
    neighborhood = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    user_id = models.ForeignKey('CustomUser', on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['user_id'], name='user_id_user_address_idx'),
            models.Index(fields=['city'], name='city_idx'),
            models.Index(fields=['state'], name='state_idx'),
        ]

    @property
    def full_address(self):
        return f'{self.street}, n° {self.number}, {self.city}-{self.state}, CEP: {self.cep}'
