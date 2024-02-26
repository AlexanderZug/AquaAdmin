from django.contrib import admin
from .models import Aquarium


@admin.register(Aquarium)
class AquariumAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "volume",
        "length",
        "width",
        "height",
        "created_at",
        "updated_at",
    )
    list_display_links = (
        "name",
        "volume",
    )
    list_filter = ("created_at",)
    search_fields = ("name",)
    date_hierarchy = "created_at"
    ordering = ("-created_at",)
    fields = (
        "name",
        "volume",
        ("length", "width", "height"),
        "created_at",
        "updated_at",
    )
