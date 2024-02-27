from django.db import models


class Aquarium(models.Model):
    name = models.CharField(
        "Aquarium Name",
        max_length=100,
        null=True,
        blank=True,
        help_text="Name des Aquariums. Falls nicht angegeben, wird ein Standardname verwendet.",
    )
    volume = models.PositiveIntegerField("Volume (L)")
    length = models.DecimalField(
        "Lange (cm)",
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    width = models.DecimalField(
        "Breite (cm)",
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    height = models.DecimalField(
        "Höhe (cm)",
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    created_at = models.DateField(
        "Erstellt am",
        help_text="Datum der Erstellung.",
    )
    updated_at = models.DateField(
        "Redesigned am",
        null=True,
        blank=True,
        help_text="Datum des letzten Redesigns, falls zutreffend.",
    )

    def __str__(self):
        return self.name if self.name else "-"

    class Meta:
        verbose_name = "Aquarium"
        verbose_name_plural = "Aquarien"
        ordering = ["-created_at"]

    def set_default_name(self):
        if not self.name:
            self.name = "-"
            self.save()
