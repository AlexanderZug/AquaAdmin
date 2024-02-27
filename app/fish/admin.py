from django.contrib import admin

from .models import Fish, Sale, Died


class SaleInline(admin.TabularInline):
    model = Sale
    extra = 1
    readonly_fields = ("total_price",)

    @admin.display(description="Gesamtpreis (€)")
    def total_price(self, obj):
        return obj.total_price

    def has_add_permission(self, request, obj=None):
        if Fish.objects.filter(pk=obj.pk, is_available=False).exists():
            return False
        return True


class DiedInline(admin.TabularInline):
    model = Died
    extra = 1


@admin.register(Fish)
class FishAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "amount",
        "created_at",
        "is_available",
    )
    list_display_links = (
        "name",
        "amount",
    )
    list_filter = ("created_at",)
    search_fields = ("name",)
    date_hierarchy = "created_at"
    ordering = ("-created_at",)
    fields = (
        "name",
        "amount",
        "image",
        "created_at",
        "is_available",
    )
    inlines = [SaleInline, DiedInline]
