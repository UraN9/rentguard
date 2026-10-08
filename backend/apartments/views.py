from rest_framework import viewsets

from .models import Apartment
from .serializers import ApartmentSerializer


class ApartmentViewSet(viewsets.ModelViewSet):
    """CRUD for apartments. A user only ever sees their own apartments."""

    serializer_class = ApartmentSerializer

    def get_queryset(self):
        return Apartment.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)