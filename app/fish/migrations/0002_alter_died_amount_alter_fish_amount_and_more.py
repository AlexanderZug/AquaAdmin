# Generated by Django 5.0.2 on 2024-02-27 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fish", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="died",
            name="amount",
            field=models.PositiveIntegerField(
                help_text="Anzahl der verstorbenen Fische.", verbose_name="Anzahl"
            ),
        ),
        migrations.AlterField(
            model_name="fish",
            name="amount",
            field=models.PositiveIntegerField(
                help_text="Anzahl der Fische.", verbose_name="Anzahl"
            ),
        ),
        migrations.AlterField(
            model_name="fish",
            name="is_available",
            field=models.BooleanField(
                default=True,
                help_text="Verfügbarkeit des Fisches.",
                verbose_name="Verfügbar",
            ),
        ),
        migrations.AlterField(
            model_name="sale",
            name="amount",
            field=models.PositiveIntegerField(
                help_text="Anzahl der verkauften Fische.", verbose_name="Anzahl"
            ),
        ),
    ]
