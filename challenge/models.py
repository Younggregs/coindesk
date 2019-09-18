# cookbook/ingredients/models.py
from django.db import models

class CoinDesk(models.Model):
    code = models.CharField(max_length=3)
    rate = models.TextField()
    description = models.CharField(max_length=50)
    rate_float = models.IntegerField()

    def __str__(self):
        return self.rate
