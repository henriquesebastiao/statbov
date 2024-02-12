from django.db import models


class WeightLog(models.Model):
    class Topic(models.TextChoices):
        ROUTINE = 'RT', 'Rotina'
        WEANING = 'WN', 'Desmame'
        BIRTH = 'BR', 'Nascimento'

    animal_id = models.ForeignKey('Animal', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    topic = models.CharField(max_length=2, choices=Topic.choices)

    class Meta:
        indexes = [
            models.Index(
                fields=['animal_id'], name='animal_id_weight_log_idx'
            ),
            models.Index(fields=['date'], name='date_weight_log_idx'),
            models.Index(fields=['topic'], name='topic_idx'),
        ]
        unique_together = ['animal_id', 'date']

    def __str__(self):
        return f'{self.date} - {self.animal_id} - {self.weight}'
