from datetime import date

from django.db import models


class Farmer(models.Model):
    class FarmerPlan(models.TextChoices):
        FREE = 'FR', 'Grátis'
        STARTER = 'ST', 'Iniciante'
        MEDIUM = 'MD', 'Médio'
        PRO = 'PR', 'Profissional'

    user_id = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11, unique=True)
    entry_date = models.DateField(auto_now_add=True)
    farmer_plan = models.CharField(max_length=2, choices=FarmerPlan.choices)

    class Meta:
        indexes = [
            models.Index(fields=['user_id'], name='user_id_farmer_idx'),
            models.Index(fields=['cpf'], name='cpf_idx'),
            models.Index(fields=['farmer_plan'], name='farmer_plan_idx'),
        ]
        unique_together = ['user_id', 'cpf', 'farmer_plan']

    @property
    def formatted_cpf(self):
        return f'{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}'

    @property
    def registration_time(self):
        today = date.today()
        return (
            today.year
            - self.entry_date.year
            - (
                (today.month, today.day)
                < (self.entry_date.month, self.entry_date.day)
            )
        )
