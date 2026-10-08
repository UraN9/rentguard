from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import RegisterSerializer, UserSerializer


class RegisterView(generics.CreateAPIView):
    """Public endpoint for creating a new account."""

    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class MeView(generics.RetrieveUpdateAPIView):
    """Read or update the profile of the authenticated user."""

    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
        