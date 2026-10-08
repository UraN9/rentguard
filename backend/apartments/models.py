from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


class Apartment(models.Model):
    """An apartment rented by a user."""

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='apartments')
    title = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    area_m2 = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(0)])
    rooms_count = models.PositiveSmallIntegerField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return str(self.title)