from __future__ import annotations

from typing import Union

from django.db import models
from django.db.models import Manager


class Fish(models.Model):
    name = models.CharField(
        "Name des Fisches",
        max_length=100,
        help_text="Name des Fisches.",
    )
    amount = models.PositiveIntegerField(
        "Anzahl",
        help_text="Anzahl der Fische.",
    )
    image = models.ImageField(
        "Bild",
        upload_to="fish/",
        null=True,
        blank=True,
        help_text="Bild des Fisches.",
    )
    created_at = models.DateField(
        "Gesetzt am",
        help_text="Datum der Setzung.",
    )
    is_available = models.BooleanField(
        "Verfügbar",
        default=True,
        help_text="Verfügbarkeit des Fisches.",
    )

    sales: Union[Sale, Manager]
    died: Union[Died, Manager]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.amount == 0:
            self.is_available = False
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Fisch"
        verbose_name_plural = "Fische"
        ordering = ["-created_at"]


class Sale(models.Model):
    fish = models.ForeignKey(
        Fish,
        on_delete=models.CASCADE,
        verbose_name="Fisch",
        related_name="sales",
    )
    amount = models.PositiveIntegerField(
        "Anzahl",
        help_text="Anzahl der verkauften Fische.",
    )
    price = models.DecimalField(
        "Preis (€)",
        max_digits=10,
        decimal_places=2,
        help_text="Preis des Fisches.",
    )
    created_at = models.DateField(
        "Verkauft am",
        help_text="Datum des Verkaufs.",
    )

    def __str__(self):
        return self.fish.name

    @property
    def total_price(self):
        if self.amount is None or self.price is None:
            return 0
        return self.amount * self.price

    def save(self, *args, **kwargs):
        self.fish.amount -= self.amount
        self.fish.save()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Verkauf"
        verbose_name_plural = "Verkäufe"
        ordering = ["-created_at"]


class Died(models.Model):
    fish = models.ForeignKey(
        Fish,
        on_delete=models.CASCADE,
        verbose_name="Fisch",
        related_name="died",
    )
    amount = models.PositiveIntegerField(
        "Anzahl",
        help_text="Anzahl der verstorbenen Fische.",
    )
    created_at = models.DateField(
        "Gestorben am",
        help_text="Datum des Todes.",
    )

    def __str__(self):
        return self.fish.name

    def save(self, *args, **kwargs):
        self.fish.amount -= self.amount
        self.fish.save()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Tod"
        verbose_name_plural = "Tode"
        ordering = ["-created_at"]
