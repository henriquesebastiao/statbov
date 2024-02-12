from django.db import models


class Diet(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=254)

    def __str__(self):
        return self.name
