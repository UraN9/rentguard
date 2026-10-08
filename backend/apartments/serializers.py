from rest_framework import serializers

from .models import Apartment


class ApartmentSerializer(serializers.ModelSerializer):
    """Serializer for apartments. The owner is set from the request, not the client."""

    class Meta:
        model = Apartment
        fields = (
            'id', 'title', 'city', 'address', 'area_m2',
            'rooms_count', 'notes', 'created_at', 'updated_at',
        )
        read_only_fields = ('id', 'created_at', 'updated_at')