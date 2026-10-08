from django.contrib import admin

from .models import Apartment


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    """Admin configuration for apartments."""

    list_display = ('title', 'city', 'owner', 'created_at')
    list_filter = ('city',)
    search_fields = ('title', 'address', 'owner__email')