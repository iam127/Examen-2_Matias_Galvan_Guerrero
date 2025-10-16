from django.db import models

class Airline(models.Model):
    """Modelo para Aerolíneas"""
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Aerolínea'
        verbose_name_plural = 'Aerolíneas'

    def __str__(self):
        return f"{self.name} ({self.country})"


class Flight(models.Model):
    """Modelo para Vuelos"""
    flight_code = models.CharField(max_length=10, unique=True)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    airline = models.ForeignKey(
        Airline, 
        on_delete=models.CASCADE, 
        related_name='flights'
    )
    departure_time = models.DateTimeField(null=True, blank=True)
    arrival_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Vuelo'
        verbose_name_plural = 'Vuelos'

    def __str__(self):
        return f"{self.flight_code}: {self.origin} → {self.destination}"