from datetime import date

from django.db import models


class Animal(models.Model):
    class AnimalRace(models.TextChoices):
        NELORE = 'NL', 'Nelore'
        GIROLANDO = 'GR', 'Girolando'
        GUZERA = 'GZ', 'Guzerá'
        HOLANDES = 'HL', 'Holandês'
        SENEPOL = 'SN', 'Senepol'
        GIR_LEITEIRO = 'GL', 'Gir Leiteiro'

    class AnimalReasonLiving(models.TextChoices):
        SALE = 'SL', 'Venda'
        DEATH = 'DT', 'Morte'
        SLAUGHTER = 'ST', 'Abate'

    id = models.CharField(max_length=15, primary_key=True)
    farm_origin_id = models.ForeignKey(
        'Farm', null=True, on_delete=models.SET_NULL
    )
    race = models.CharField(max_length=2, choices=AnimalRace.choices)
    mother_id = models.ForeignKey(
        'self', null=True, on_delete=models.SET_NULL, related_name='mother'
    )
    father_id = models.ForeignKey(
        'self', null=True, on_delete=models.SET_NULL, related_name='father'
    )
    gender = models.CharField(max_length=1)
    entry_date = models.DateField(auto_now_add=True)
    exit_date = models.DateField(null=True, blank=True)
    reason_living = models.CharField(
        max_length=2, choices=AnimalReasonLiving.choices, null=True, blank=True
    )

    class Meta:
        indexes = [
            models.Index(fields=['farm_origin_id'], name='farm_origin_id_idx'),
            models.Index(fields=['race'], name='race_idx'),
            models.Index(fields=['mother_id'], name='mother_id_idx'),
            models.Index(fields=['father_id'], name='father_id_idx'),
            models.Index(fields=['gender'], name='gender_idx'),
            models.Index(fields=['entry_date'], name='entry_date_idx'),
            models.Index(fields=['exit_date'], name='exit_date_idx'),
            models.Index(fields=['reason_living'], name='reason_living_idx'),
        ]

    def __str__(self):
        return f'{self.id} - {self.race} - {self.gender}'

    @property
    def entry_time(self):
        if not self.exit_date:
            today = date.today()
            return (
                today.year
                - self.entry_date.year
                - (
                    (today.month, today.day)
                    < (self.entry_date.month, self.entry_date.day)
                )
            )
        return 0
