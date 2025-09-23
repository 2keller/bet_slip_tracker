from typing import Any
from django.db import models

# Create your models here.
class Betslip(models.Model):
    slip_code = models.CharField(max_length=100)
    bookmaker = models.CharField(max_length=100)
    status = models.CharField(max_length=20,  default='pending')
    checked_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.bookmaker} - {self.slip_code}"